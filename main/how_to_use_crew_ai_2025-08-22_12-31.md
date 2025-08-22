# Getting Started with CrewAI: A Beginner's Guide

## What is CrewAI?

CrewAI is a framework for orchestrating autonomous AI agents to work collaboratively on complex tasks. It allows you to build virtual teams of experts, each with unique skills and responsibilities, all powered by large language models (LLMs). It's ideal for projects that demand reasoning, planning, and collaboration.

## Installation

Before you can start building your AI crew, you'll need to install the `crewai` package using pip:

```bash
pip install crewai
```

You'll also need an LLM API key. CrewAI supports various LLMs, including OpenAI, Ollama, and others. This guide assumes you're using OpenAI. Ensure you have an OpenAI API key and set it as an environment variable:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Building Your First Crew

Let's create a simple crew consisting of two agents: a Research Agent and a Writing Agent.

### Defining the Agents

First, define the roles and tools for each agent.

```python
from crewai import Agent
from tools.search_tool import SearchTool  # Assuming you have a SearchTool

researcher = Agent(
    role='Research Agent',
    goal='Gather information and insights about a given topic.',
    backstory="You are a highly skilled research agent with expertise in gathering information from various sources.",
    tools=[SearchTool()],  # You'll need to define or import a search tool
    verbose=True,  # Set to True to see the agent's thought process
    allow_delegation=False
)

writer = Agent(
    role='Writing Agent',
    goal='Write a compelling and informative article based on the research provided.',
    backstory="You are an experienced writer with a knack for crafting engaging content.",
    verbose=True,
    allow_delegation=False
)
```

**Key Considerations:**

*   You'll need to define or import `SearchTool`. A basic search tool example could use the `duckduckgo_search` package. (See example below)
*   `verbose=True` is useful for debugging and understanding how your agents are reasoning.
*   `allow_delegation=False` prevents agents from delegating tasks to each other in this example.

### Creating the Crew

Now that we have our agents, let's create the crew and assign them tasks.

```python
from crewai import Crew, Task

# Define the tasks for each agent
research_task = Task(
    description="Research the latest advancements in renewable energy, focusing on solar and wind power.",
    agent=researcher
)

write_task = Task(
    description="Write a concise and informative article about the advancements in renewable energy based on the research provided.",
    agent=writer
)

# Assemble the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=2  # Set to 2 to see the crew's plan
)
```

### Running the Crew

Finally, run the crew and observe the results!

```python
result = crew.kickoff()

print(result)
```

The `kickoff()` method starts the crew, and the `result` will be the final output of the process  in this case, the article written by the Writing Agent.

## Implementing a Basic Search Tool (Example)

As mentioned earlier, you'll need a search tool. Here's a basic example using `duckduckgo_search`. First, install it:

```bash
pip install duckduckgo_search
```

Then, create a file named `tools/search_tool.py` (or adjust the import statement accordingly) with the following content:

```python
from duckduckgo_search import ddg_search
from typing import List

class SearchTool():
    name = "Search the internet"
    description = "Useful for when you need to answer questions about current events. Input should be a search query."

    def run(self, query: str) -> str:
        """Use the tool."""
        results = ddg_search(query)
        return str(results)
```

## Going Further

This is a basic example to get you started. CrewAI offers many more advanced features, including:

*   **Complex agent interactions:** Agents can delegate tasks, debate, and collaborate more deeply.
*   **Sophisticated tools:** Integrate with various APIs and services.
*   **Customizable agent personalities:** Define detailed backstories and personalities.
*   **Parallel task execution:** Run tasks concurrently for faster results.

Experiment with different agent roles, tasks, and tools to create powerful AI crews that can tackle complex problems. Happy building!