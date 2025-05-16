import os
from crewai import BaseTool, tool
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.generativeai as genai
import requests
import json

# --- Utility Functions (Can be used by Tools) ---

def get_sheet_service(credentials_path):
    """Authenticates and returns the Google Sheets service."""
    try:
        creds = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly'] # Readonly scope is sufficient
        )
        service = build('sheets', 'v4', credentials=creds)
        print("Utility: Google Sheets service connected successfully.")
        return service
    except FileNotFoundError:
        print(f"Utility Error: credentials.json not found at {credentials_path}")
        return None
    except Exception as e:
        print(f"Utility Error connecting to Google Sheets: {e}")
        return None

def get_ai_model(api_key):
    """Configures and returns the Google Generative AI model."""
    if not api_key:
        print("Utility Error: GOOGLE_API_KEY not provided.")
        return None
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro') # Or 'gemini-1.5-pro-latest' etc.
        print("Utility: Google AI model configured successfully.")
        return model
    except Exception as e:
        print(f"Utility Error configuring Google AI model: {e}")
        return None

# --- Custom Tools for Crew AI ---

class GoogleSheetReaderTool(BaseTool):
    name: str = "Google Sheet Reader Tool"
    description: str = "Reads text content from a specific cell or range in a Google Sheet. Input should be the sheet ID and the cell/range reference (e.g., 'Sheet1!A5')."
    sheets_service: any # Type hint for the Sheets service object

    def __init__(self, sheets_service, **kwargs):
         super().__init__(**kwargs)
         self.sheets_service = sheets_service

    def _run(self, sheet_input: str) -> str:
        """
        Args:
            sheet_input (str): A string containing the sheet ID and range, separated by a comma or space,
                                OR just the range if sheet ID is implicitly known by the tool (less flexible).
                                Let's assume input is 'SHEET_ID,Sheet1!A5' or 'SHEET_ID Sheet1!A5'.
                                Or simply the range 'Sheet1!A5' if the sheet ID is handled during tool instantiation.
                                Let's design it to take 'SHEET_ID,RANGE'.
        """
        try:
            # Assuming input is 'SHEET_ID,RANGE'
            parts = sheet_input.split(',')
            if len(parts) != 2:
                 return f"Error: Invalid input format for GoogleSheetReaderTool. Expected 'SHEET_ID,RANGE', got '{sheet_input}'"

            sheet_id = parts[0].strip()
            sheet_range = parts[1].strip()


            if not self.sheets_service:
                return "Error: Google Sheets service not initialized."

            print(f"Tool: Reading from sheet ID '{sheet_id}', range '{sheet_range}'...")
            result = self.sheets_service.spreadsheets().values().get(
                spreadsheetId=sheet_id, range=sheet_range
            ).execute()
            values = result.get('values', [])

            if not values:
                print(f"Tool: No data found in range: {sheet_range}")
                return f"Error: No data found in range: {sheet_range}"
            else:
                 # Assuming we read a single cell or want the first cell's value
                 # If values is [['Content']], this gets 'Content'
                 # If values is [['Content1', 'Content2']], this gets 'Content1'
                 # Adjust if you need to concatenate multiple cells from the row
                sheet_text = values[0][0] if values and values[0] else ""
                print(f"Tool: Successfully read text from sheet: '{sheet_text[:50]}...' (truncated)") # Print start of text
                return sheet_text.strip()

        except HttpError as err:
            print(f"Tool Error: Google Sheets API error: {err}")
            return f"Error reading Google Sheet: {err}"
        except Exception as e:
            print(f"Tool Error reading from Google Sheet: {e}")
            return f"Error reading Google Sheet: {e}"


class GoogleAIGeneratorTool(BaseTool):
    name: str = "Google AI Generator Tool"
    description: str = "Generates text content using the Google AI (Gemini) model based on input text. Input should be the text to process."
    ai_model: any # Type hint for the AI model object
    prompt_prefix: str
    prompt_suffix: str

    def __init__(self, ai_model, prompt_prefix="", prompt_suffix="", **kwargs):
        super().__init__(**kwargs)
        self.ai_model = ai_model
        self.prompt_prefix = prompt_prefix
        self.prompt_suffix = prompt_suffix

    def _run(self, text_input: str) -> str:
        """
        Args:
            text_input (str): The text content to be used as input for the AI model.
        """
        if not self.ai_model or not text_input:
            return "Error: AI model not initialized or input text is empty."

        try:
            full_prompt = f"{self.prompt_prefix}{text_input}{self.prompt_suffix}".strip()

            if not full_prompt:
                 print("Tool Warning: Resulting prompt is empty.")
                 return "Error: Empty prompt provided to AI."

            print(f"Tool: Sending prompt to AI: '{full_prompt[:100]}...' (truncated)")
            response = self.ai_model.generate_content(full_prompt)

            if response.text:
                ai_output = response.text.strip()
                print("Tool: AI generated content successfully.")
                return ai_output
            else:
                print("Tool Error: AI response received, but no text content found.")
                print(f"Tool: AI Response Feedback: {response.prompt_feedback}")
                # Return detailed error if available
                return f"Error: AI did not return text content. Feedback: {response.prompt_feedback}"

        except Exception as e:
            print(f"Tool Error generating AI content: {e}")
            return f"Error generating AI content: {e}"


class DiscordPosterTool(BaseTool):
    name: str = "Discord Poster Tool"
    description: str = "Sends a text message to a Discord channel using a webhook. Input should be the message text to post."
    webhook_url: str

    def __init__(self, webhook_url, **kwargs):
        super().__init__(**kwargs)
        self.webhook_url = webhook_url

    def _run(self, message: str) -> str:
        """
        Args:
            message (str): The text message content to send to Discord.
                           Note: Discord has message length limits (typically 2000 characters).
        """
        if not self.webhook_url:
            return "Error: Discord webhook URL not provided."
        if not message:
             return "Error: Cannot send empty message to Discord."

        # Truncate message if too long for Discord (optional, adjust as needed)
        # Discord max length for 'content' is 2000 characters
        if len(message) > 2000:
            print(f"Tool Warning: Message exceeds Discord limit ({len(message)} > 2000). Truncating.")
            message = message[:1997] + "..." # Truncate and add ellipsis

        payload = {"content": message}
        headers = {'Content-Type': 'application/json'}

        try:
            print("Tool: Sending message to Discord...")
            response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            print("Tool: Message sent to Discord successfully.")
            return "Successfully posted message to Discord."
        except requests.exceptions.RequestException as e:
            print(f"Tool Error sending message to Discord: {e}")
            return f"Error sending message to Discord: {e}"