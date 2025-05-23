# Getting Started with CrewAI: Building Intelligent Agent Teams

## What is CrewAI?

CrewAI is a framework for orchestrating autonomous AI agents that work together in role-playing teams. It allows you to build teams of agents to accomplish complex tasks, essentially creating your own AI-powered think tank!

## Installation

Before you start, install the `crewai` package. Open your terminal and run:

```bash
pip install crewai
```

You'll also need an OpenAI API key or another LLM provider configured. Ensure you have the `openai` package installed:

```bash
pip install openai
```

Then, set your API key as an environment variable:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Building Your First Crew

Let's create a simple crew with two agents: a Researcher and a Writer.

### Defining Agents

First, define your agents. Each agent has a role, a goal, and access to tools.

```python
from crewai import Agent
from tools.search_tool import SearchTool  # Assuming you have a SearchTool

researcher = Agent(
    role='Researcher',
    goal='Gather information about the latest AI trends',
    backstory="""An expert in AI research, always up-to-date with the latest advancements.
    You have a knack for finding hidden gems in research papers and articles.""",
    verbose=True,  # Will print details about what the agent is doing
    allow_delegation=False,
    tools=[SearchTool()]
)

writer = Agent(
    role='Writer',
    goal='Write compelling blog posts about AI',
    backstory="""A seasoned tech blogger with a passion for making complex topics easy to understand.
    You are skilled at crafting engaging narratives and simplifying technical jargon.""",
    verbose=True,
    allow_delegation=True
)
```

Here's a breakdown of the agent parameters:

*   `role`: The agent's job title within the crew.
*   `goal`: The agent's objective.
*   `backstory`: Gives the agent a persona and context.
*   `verbose`: Enables detailed logging of the agent's activities. Useful for debugging and understanding the agent's thought process.
*   `allow_delegation`: Determines if the agent can delegate tasks to other agents.
*   `tools`: A list of tools the agent can use.

**Important:** The example above assumes you have a `SearchTool` defined. Here's a basic implementation using DuckDuckGo Search:

```python
from crewai import Tool
from duckduckgo_search import ddg

class SearchTool(Tool):
    name = "Search the web"
    description = "Useful for when you need to answer questions about current events. Input should be a search query."
    def _run(self, query: str) -> str:
        return ddg(query)
```

You'll need to install `duckduckgo_search`:

```bash
pip install duckduckgo_search
```

### Defining Tasks

Next, define the tasks for each agent.

```python
from crewai import Task

research_task = Task(
    description="""Identify the top 3 most impactful AI trends of 2024.
    Focus on trends with significant real-world applications and potential for disruption.""",
    agent=researcher
)

write_task = Task(
    description="""Write a blog post summarizing the AI trends identified by the researcher.
    The blog post should be engaging, informative, and easy to understand for a general audience.
    Include examples of real-world applications and potential impacts.""",
    agent=writer
)
```

Here's a breakdown of the task parameters:

*   `description`: A clear and concise description of the task. The more specific you are, the better the agent will perform.
*   `agent`: The agent assigned to perform the task.

### Creating the Crew

Now, assemble the crew.

```python
from crewai import Crew

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=2  # You can set it to 1 or 2 for different logging levels
)
```

Here's a breakdown of the crew parameters:

*   `agents`: A list of the agents in the crew.
*   `tasks`: A list of the tasks the crew will perform.
*   `verbose`: Controls the level of logging. `2` provides the most detailed output.

### Running the Crew

Finally, run the crew and let the agents do their work!

```python
result = crew.kickoff()

print("Final Result:")
print(result)
```

The `kickoff()` method starts the crew and orchestrates the agents to complete their tasks. The result will be the final output of the crew, in this case, the generated blog post.

## Putting It All Together

Here's the complete code:

```python
import os
from crewai import Crew, Agent, Task, Tool
from duckduckgo_search import ddg

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

class SearchTool(Tool):
    name = "Search the web"
    description = "Useful for when you need to answer questions about current events. Input should be a search query."
    def _run(self, query: str) -> str:
        return ddg(query)

# Define agents
researcher = Agent(
    role='Researcher',
    goal='Gather information about the latest AI trends',
    backstory="""An expert in AI research, always up-to-date with the latest advancements.
    You have a knack for finding hidden gems in research papers and articles.""",
    verbose=True,
    allow_delegation=False,
    tools=[SearchTool()]
)

writer = Agent(
    role='Writer',
    goal='Write compelling blog posts about AI',
    backstory="""A seasoned tech blogger with a passion for making complex topics easy to understand.
    You are skilled at crafting engaging narratives and simplifying technical jargon.""",
    verbose=True,
    allow_delegation=True
)

# Define tasks
research_task = Task(
    description="""Identify the top 3 most impactful AI trends of 2024.
    Focus on trends with significant real-world applications and potential for disruption.""",
    agent=researcher
)

write_task = Task(
    description="""Write a blog post summarizing the AI trends identified by the researcher.
    The blog post should be engaging, informative, and easy to understand for a general audience.
    Include examples of real-world applications and potential impacts.""",
    agent=writer
)

# Create crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=2
)

# Run crew
result = crew.kickoff()

print("Final Result:")
print(result)
```

Remember to replace `"YOUR_OPENAI_API_KEY"` with your actual OpenAI API key.

## Advanced Usage

CrewAI offers many more advanced features, including:

*   **Different LLMs:** You can use other LLMs besides OpenAI's, such as Mistral or even local models.
*   **Custom Tools:** Create your own tools tailored to specific tasks.
*   **Complex Workflows:** Define intricate task dependencies and agent interactions.
*   **Memory Management:** Give agents the ability to remember past interactions and learn over time.
*   **Hierarchical Crews:** Nest crews within crews for even more complex projects.

Explore the CrewAI documentation for more details and examples: [https://www.crewai.com/](https://www.crewai.com/)