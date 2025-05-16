import os
from dotenv import load_dotenv
import sys # To read command-line arguments
from crewai import Crew, Process

# Import agents, tasks, and tools
from tools import get_sheet_service, get_ai_model, GoogleSheetReaderTool, GoogleAIGeneratorTool, DiscordPosterTool
from agents import BlogAutomationAgents
from tasks import BlogAutomationTasks

# Load environment variables
load_dotenv()

# --- Configuration ---
GOOGLE_SHEETS_CREDENTIALS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
BLOG_COLUMN_LETTER = os.getenv("BLOG_COLUMN_LETTER", "A") # Default to column A
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PROMPT_PREFIX = os.getenv("PROMPT_PREFIX", "")
PROMPT_SUFFIX = os.getenv("PROMPT_SUFFIX", "")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# --- Read Command Line Argument ---
if len(sys.argv) != 2:
    print("Usage: python main.py <row_number>")
    sys.exit(1)

try:
    row_number = int(sys.argv[1])
    if row_number <= 0:
         raise ValueError("Row number must be positive.")
except ValueError as e:
    print(f"Error: Invalid row number. {e}")
    print("Usage: python main.py <row_number>")
    sys.exit(1)

print(f"Attempting to process row number: {row_number}")


# --- Initialize Services and Tools ---
print("Initializing services and tools...")

# Google Sheets Service
sheets_service = get_sheet_service(GOOGLE_SHEETS_CREDENTIALS_PATH)
if not sheets_service:
    print("Failed to initialize Google Sheets service.")
    sys.exit(1)
sheet_reader_tool = GoogleSheetReaderTool(sheets_service=sheets_service)


# Google AI Model
ai_model = get_ai_model(GOOGLE_API_KEY)
if not ai_model:
    print("Failed to initialize Google AI model.")
    sys.exit(1)
ai_generator_tool = GoogleAIGeneratorTool(
    ai_model=ai_model,
    prompt_prefix=PROMPT_PREFIX,
    prompt_suffix=PROMPT_SUFFIX
)

# Discord Poster Tool
if not DISCORD_WEBHOOK_URL:
    print("Discord webhook URL not configured.")
    # Decide if this is a fatal error or if you proceed without posting
    # For this example, we'll make it fatal if posting is required.
    print("DISCORD_WEBHOOK_URL is missing. Cannot send to Discord.")
    sys.exit(1)
discord_poster_tool = DiscordPosterTool(webhook_url=DISCORD_WEBHOOK_URL)


# --- Create Agents ---
print("Creating agents...")
agent_manager = BlogAutomationAgents(
    sheet_reader_tool=sheet_reader_tool,
    ai_generator_tool=ai_generator_tool,
    discord_poster_tool=discord_poster_tool
)

sheet_reader = agent_manager.sheet_reader_agent()
content_processor = agent_manager.content_processor_agent()
discord_poster = agent_manager.discord_poster_agent()


# --- Create Tasks ---
print("Creating tasks...")
task_manager = BlogAutomationTasks(agents=agent_manager)

# The read task needs the specific row number
read_task = task_manager.read_blog_content_task(
    sheet_id=GOOGLE_SHEET_ID,
    blog_column_letter=BLOG_COLUMN_LETTER,
    row_number=row_number
)

# Process and post tasks get their input from the output of the previous task via context
process_task = task_manager.process_blog_content_task()
post_task = task_manager.post_to_discord_task()


# --- Create and Run Crew ---
print("Creating and running crew...")
crew = Crew(
    agents=[sheet_reader, content_processor, discord_poster],
    tasks=[read_task, process_task, post_task],
    process=Process.sequential, # Tasks run one after another
    verbose=True # Set to True to see detailed agent execution
)

# The kickoff method starts the crew.
# The `inputs` dictionary can pass initial variables to tasks if they are defined using {variable_name} in the task description.
# In our case, we constructed the sheet_range directly when creating the read_task,
# and subsequent tasks use `context`, so no extra inputs are needed here.
print("Crew kickoff initiated...")
result = crew.kickoff()

print("\n--- Crew Execution Finished ---")
print("Final Result of the Crew:")
print(result) # The final result is typically the output of the last task.