from crewai import Task
from .agents import BlogAutomationAgents
from crewai import Task


D:\vaibhav\PROJECT\RC-Project\downloads\crew\tasks.py

class BlogAutomationTasks:
    def __init__(self, agents: BlogAutomationAgents):
        self.agents = agents

    def read_blog_content_task(self, sheet_id: str, blog_column_letter: str, row_number: int) -> Task:
        """
        Task to read blog content from a specific cell in a Google Sheet.
        The input will be used to tell the agent which range to read.
        """
        sheet_range = f"Sheet1!{blog_column_letter}{row_number}" # Assuming sheet name is 'Sheet1'

        return Task(
            description=f"Read the blog content from the Google Sheet at range '{sheet_range}'. "
                        f"Use the Google Sheet Reader Tool with input '{sheet_id},{sheet_range}'.",
            expected_output=f"The raw text content read from cell '{sheet_range}'. "
                            "If no content is found, return an explicit message like 'No content found in Sheet1!A5'.",
            agent=self.agents.sheet_reader_agent(),
            # Pass the input needed by the tool via the task description or as direct input if using task.execute
            # For Crew orchestration, relying on the description and tool input parsing is common.
            # Alternatively, you could pass it via `inputs` to crew.kickoff and reference with {variable_name}
            # Let's make the description explicit for the agent.
        )

    def process_blog_content_task(self) -> Task:
        """
        Task to process the raw blog content using the AI model.
        This task takes the output from the previous reading task as context.
        """
        return Task(
            description="Take the raw blog content provided from the previous task. "
                        "Use the Google AI Generator Tool to transform this content into a polished and engaging blog post. "
                        "Ensure the output is the final, refined blog post text.",
            expected_output="The complete, AI-generated blog post text, ready for publication. "
                            "Do NOT include any conversational text like 'Here is the blog post:'. "
                            "Just provide the markdown/text of the post itself.",
            agent=self.agents.content_processor_agent(),
            context=[self.read_blog_content_task] # This task uses the output of the read task
        )

    def post_to_discord_task(self) -> Task:
        """
        Task to post the final AI-generated blog post to Discord.
        This task takes the output from the content processing task as context.
        """
        return Task(
            description="Take the final AI-generated blog post text provided from the previous task. "
                        "Use the Discord Poster Tool to publish this text to the configured Discord channel.",
            expected_output="A confirmation message indicating that the message was successfully sent to Discord, "
                            "or an error message if the posting failed.",
            agent=self.agents.discord_poster_agent(),
            context=[self.process_blog_content_task] # This task uses the output of the AI task
        )