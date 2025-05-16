import os
from dotenv import load_dotenv
import requests
import json

# Google Sheets API libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# LangChain libraries
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
GOOGLE_SHEETS_CREDENTIALS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_SHEET_RANGE = os.getenv("GOOGLE_SHEET_RANGE")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_AI_MODEL = os.getenv("GOOGLE_AI_MODEL", "gemini-pro") # Default to gemini-pro
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
BLOG_GENERATION_PROMPT_TEMPLATE = os.getenv(
    "BLOG_GENERATION_PROMPT_TEMPLATE",
    "Expand the following raw text into a blog post: {raw_text}" # Default template
)


# --- Google Sheets Functions (Same as previous script) ---
def get_sheet_service():
    """Authenticates and returns the Google Sheets service."""
    try:
        creds = service_account.Credentials.from_service_account_file(
            GOOGLE_SHEETS_CREDENTIALS_PATH,
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )
        service = build('sheets', 'v4', credentials=creds)
        print("Google Sheets service connected successfully.")
        return service
    except FileNotFoundError:
        print(f"Error: credentials.json not found at {GOOGLE_SHEETS_CREDENTIALS_PATH}")
        return None
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")
        return None

def read_sheet_range(service, sheet_id, sheet_range):
    """Reads data from a specified range in a Google Sheet."""
    if not service:
        return None

    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=sheet_range
        ).execute()
        values = result.get('values', [])

        if not values:
            print(f"No data found in range: {sheet_range}")
            return None
        else:
             # Simple handling: take the first non-empty cell's value found
             # Adjust this if your input structure is different
            sheet_text_parts = [cell for row in values for cell in row if cell]
            sheet_text = " ".join(sheet_text_parts).strip()
            print(f"Read from sheet ('{sheet_range}'): {sheet_text}")
            return sheet_text if sheet_text else None # Return None if empty after stripping


    except HttpError as err:
        print(f"Google Sheets API error: {err}")
        return None
    except Exception as e:
        print(f"Error reading from Google Sheet: {e}")
        return None

# --- Custom LangChain Tool for Google AI Blog Generation ---

# We use the @tool decorator to easily define a LangChain tool from a Python function.
# The function's docstring becomes the tool's description, and its parameters become inputs.
@tool
def generate_blog_from_text(raw_text: str) -> str:
    """
    Generates a comprehensive and detailed blog post based on the provided raw text input.
    Useful for expanding notes or short descriptions into full articles.
    Input should be the raw text content that needs to be expanded into a blog post.
    """
    if not GOOGLE_API_KEY:
        return "Error: GOOGLE_API_KEY not configured for AI generation tool."

    if not raw_text:
        return "Error: No raw text provided to the blog generation tool."

    try:
        # Instantiate the LLM *within the tool* for its specific task
        # This LLM instance is used *by the tool* to generate the blog content,
        # separate from the LLM used by the agent for reasoning.
        llm_generator = ChatGoogleGenerativeAI(
            model=GOOGLE_AI_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=0.7 # Example: adjust creativity
        )

        # Format the prompt using the template from .env
        prompt_text = BLOG_GENERATION_PROMPT_TEMPLATE.format(raw_text=raw_text)

        print("Tool 'generate_blog_from_text': Calling LLM for generation...")
        # Use .invoke for a single call
        response = llm_generator.invoke(prompt_text)
        print("Tool 'generate_blog_from_text': LLM call finished.")

        # LangChain LLM invoke returns a Message object, get the content
        if response and response.content:
            return response.content.strip()
        else:
            print("Tool 'generate_blog_from_text': LLM response received, but no content.")
            # You might want to inspect response.additional_kwargs or response.response_metadata
            return "AI tool did not return text content."

    except Exception as e:
        print(f"Tool 'generate_blog_from_text': Error during AI generation: {e}")
        return f"Tool Error: Could not generate blog content - {e}"


# --- LangChain Agent Setup ---

# Configure the main LLM used by the agent for reasoning (deciding which tool to use)
# This needs GOOGLE_API_KEY and the model name
if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in environment variables. Cannot configure Agent LLM.")
    agent_llm = None
else:
    try:
        # Agent LLM typically doesn't need high temperature as it focuses on function calling/reasoning
        agent_llm = ChatGoogleGenerativeAI(
            model=GOOGLE_AI_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=0
        )
        print(f"Agent LLM configured with Google AI model: {GOOGLE_AI_MODEL}")
    except Exception as e:
         print(f"Error configuring LangChain Agent LLM for Google AI: {e}")
         agent_llm = None


# Define the tools the agent can use
tools = [generate_blog_from_text] # Our custom tool

# Define the prompt template for the agent
# This guides the agent on its overall goal and how to use the tools
agent_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert content creation agent. Your goal is to take
     raw text provided by the user and use the available tools to generate a
     high-quality blog post from it."""),
    ("human", "Generate a blog post based on the following raw text: {input}"),
    ("placeholder", "{agent_scratchpad}") # Important for the agent's thinking process
])

# Create the agent
# We use create_tool_calling_agent as Gemini supports tool calling
if agent_llm:
    agent = create_tool_calling_agent(agent_llm, tools, agent_prompt)
else:
    agent = None # Cannot create agent if LLM setup failed


# Create the Agent Executor
# This is the runtime for the agent, handling the loop of thinking, tool use, and observations
if agent:
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # Set verbose=True to see the steps
else:
     agent_executor = None # Cannot create executor if agent setup failed


# --- Discord Functions (Same as previous script, with chunking) ---
def send_to_discord(webhook_url, message):
    """Sends a message to Discord via a webhook."""
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL not found in environment variables.")
        return False

    # Discord has message length limits (2000 characters). Break into chunks.
    max_discord_length = 2000
    messages_to_send = []

    if len(message) <= max_discord_length:
        messages_to_send.append(message)
    else:
        # Simple paragraph split chunking
        paragraphs = message.split('\n\n')
        current_chunk = ""
        for i, para in enumerate(paragraphs):
            # Add +2 for potential '\n\n' separator between paragraphs
            if len(current_chunk) + len(para) + (2 if current_chunk else 0) > max_discord_length:
                messages_to_send.append(current_chunk.strip())
                current_chunk = para
            else:
                current_chunk += (('\n\n' + para) if current_chunk else para)
        if current_chunk:
            messages_to_send.append(current_chunk.strip())

    print(f"Preparing to send {len(messages_to_send)} message chunk(s) to Discord.")

    success_count = 0
    for i, msg_chunk in enumerate(messages_to_send):
        payload = {"content": msg_chunk}
        try:
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
            print(f"Chunk {i+1}/{len(messages_to_send)} sent to Discord successfully.")
            success_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Error sending Discord message chunk {i+1}/{len(messages_to_send)}: {e}")
            # Optionally break or continue based on desired behavior
            # break # Stop sending remaining chunks if one fails
            pass # Continue sending other chunks

    return success_count > 0 # Return True if at least one chunk was sent


# --- Main Script Logic ---
if __name__ == "__main__":
    print("Starting script with LangChain Agent...")

    # --- Step 1: Get data from Google Sheets ---
    sheets_service = get_sheet_service()
    if not sheets_service:
        print("Failed to connect to Google Sheets. Exiting.")
        # Optionally send a Discord message about the setup failure
        send_to_discord(DISCORD_WEBHOOK_URL, "Script failed: Could not connect to Google Sheets.")
        exit()

    sheet_input_text = read_sheet_range(sheets_service, GOOGLE_SHEET_ID, GOOGLE_SHEET_RANGE)

    if not sheet_input_text:
        print("Could not read text from Google Sheet or sheet text is empty. Exiting.")
        send_to_discord(DISCORD_WEBHOOK_URL, "Script failed: Could not read text from Google Sheet or sheet text is empty.")
        exit()

    # --- Step 2: Run LangChain Agent to generate blog content ---
    # Ensure Agent Executor was configured successfully
    if not agent_executor:
        print("LangChain Agent Executor not configured correctly. Cannot run Agent. Exiting.")
        send_to_discord(DISCORD_WEBHOOK_URL, "Script failed: LangChain Agent/LLM not configured correctly (check GOOGLE_API_KEY).")
        exit()

    print("Running LangChain Agent Executor process...")
    agent_result = None
    try:
        # The AgentExecutor takes input as a dictionary
        result = agent_executor.invoke({"input": sheet_input_text})
        # The final answer from the agent is in the 'output' key of the result dictionary
        agent_result = result.get('output')

        print("\nLangChain Agent process finished.")
        print("Agent Output:")
        print(agent_result)

    except Exception as e:
        print(f"\nError during LangChain Agent execution: {e}")
        agent_result = f"LangChain Agent execution failed: {e}" # Capture the error as result

    # --- Step 3: Send the Agent result to Discord ---
    if not agent_result or agent_result.startswith("Error:") or agent_result.startswith("Tool Error:"):
         final_discord_message = f"Blog generation failed or returned no content.\nDetails: {agent_result}"
         send_to_discord(DISCORD_WEBHOOK_URL, final_discord_message)
    else:
         # Optionally add a header or formatting for Discord
         discord_message_header = "✍️ Generated Blog Post (via LangChain Agent) ✍️\n\n"
         final_discord_message = discord_message_header + agent_result

         send_to_discord(DISCORD_WEBHOOK_URL, final_discord_message)

    print("Script finished.")