from crewai import Crew, Process  # Import Crew and Process classes from crewai
from task import PrepTask  # Import PrepTask class for task definitions
from agents import PrepAgent  # Import PrepAgent class for agent definitions
from tools import SearchToolset  # Import SearchToolset for accessing tools
import os  # Standard library for environment variable management

# Asynchronous function to initialize agents and tasks for the multi-agent architecture
async def initialize_agents_and_tasks():
    # Initialize a task instance
    task = PrepTask()

    # Initialize agents instance
    agents = PrepAgent()

    # Initialize tools
    tool = SearchToolset.tool()  # Fetch the search tool (e.g., SerperDevTool)

    # Create individual agents for different roles
    research_agent = agents.Industry_Research_Agent()  # Agent for industry research
    use_case_agent = agents.Use_Cases_Generation()  # Agent for AI use case generation
    resorce_colletion = agents.Resource_Asset_Collection()  # Agent for resource asset collection

    # Create tasks and assign them to respective agents
    research_task = task.research_task(research_agent)  # Task to research the industry
    use_case_task = task.use_case_generation_task(use_case_agent)  # Task to generate AI use cases
    resorce_link = task.resource_collection_task(resorce_colletion)  # Task to collect resource links

    # Create the multi-agent system (Crew) with agents and tasks
    crew = Crew(
        agents=[research_agent, use_case_agent, resorce_colletion],  # List of agents
        tasks=[research_task, use_case_task, resorce_link],  # List of tasks
        process=Process.sequential,  # Define execution process (sequential execution)
        # memory=True  # Optional: Enable memory for persistent agent interactions
    )
    
    # Return the initialized Crew object for further processing
    return crew

# Uncomment the following code block to run standalone (for debugging or testing)
# if __name__ == "__main__":
#     initialize_agents_and_tasks()
