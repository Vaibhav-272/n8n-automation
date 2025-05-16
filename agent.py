from crewai import Agent
from .tools import GoogleSheetReaderTool, GoogleAIGeneratorTool, DiscordPosterTool

class BlogAutomationAgents:
    def __init__(self, sheet_reader_tool: GoogleSheetReaderTool,
                 ai_generator_tool: GoogleAIGeneratorTool,
                 discord_poster_tool: DiscordPosterTool):
        self.sheet_reader_tool = sheet_reader_tool
        self.ai_generator_tool = ai_generator_tool
        self.discord_poster_tool = discord_poster_tool

    def sheet_reader_agent(self) -> Agent:
        return Agent(
            role="Google Sheets Data Retriever",
            goal="Accurately fetch specific blog content from a Google Sheet using the provided range.",
            backstory=(
                "This agent is an expert in accessing and retrieving data from Google Sheets. "
                "It is precise and ensures the correct cell or range content is obtained for processing."
            ),
            tools=[self.sheet_reader_tool],
            verbose=True,
            allow_delegation=False # This agent performs a specific read task
        )

    def content_processor_agent(self) -> Agent:
        return Agent(
            role="AI Blog Content Generator",
            goal="Transform raw blog content into a polished, engaging, and ready-to-publish post using the AI model.",
            backstory=(
                "This agent is a creative writer powered by advanced AI. "
                "It specializes in taking draft content and enhancing it, improving flow, "
                "and ensuring it meets publication standards."
            ),
            tools=[self.ai_generator_tool],
            verbose=True,
            allow_delegation=False # This agent performs the core AI processing
        )

    def discord_poster_agent(self) -> Agent:
        return Agent(
            role="Discord Publication Manager",
            goal="Successfully post the final AI-generated blog content to the designated Discord channel using the webhook.",
            backstory=(
                "This agent is responsible for the final delivery step. "
                "It ensures the polished blog post is correctly formatted and sent "
                "to the Discord channel without errors."
            ),
            tools=[self.discord_poster_tool],
            verbose=True,
            allow_delegation=False # This agent performs the final posting
        )