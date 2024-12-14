from crewai import Task
from tools import SearchToolset

class PrepTask():
    # Constructor to initialize the agent
    def __int__(self, agent):
        self.agent = agent

    # Method to create a research task
    def research_task(self, agent):
        return Task(
            description="Use a web browser tool to research the company's industry, key offerings, and strategic focus.",
            expected_output="A detailed report of the company's industry, offerings, and strategic goals.",
            # Optionally include tools for web research (commented out for now)
            # tools=[SearchToolset.tool()],
            agent=agent,  # The agent responsible for performing this task
            # async_execution=False  # Indicates if the task runs synchronously or asynchronously (commented out here)
        )

    # Method to create a task for generating AI/ML use cases
    def use_case_generation_task(self, agent):
        return Task(
            description="Analyze industry trends in AI/ML and automation and propose relevant use cases for the company.",
            expected_output="A list of relevant AI/ML use cases to improve company processes and customer experiences.",
            # Optionally include tools for analysis (commented out for now)
            # tools=[SearchToolset.tool()],
            agent=agent,  # The agent responsible for performing this task
            output_file='use-cases.md',  # File where the output will be saved
            # async_execution=False  # Indicates if the task runs synchronously or asynchronously (commented out here)
        )

    # Method to create a task for collecting resource assets
    def resource_collection_task(self, agent):
        return Task(
            description="Search for relevant datasets for the proposed use cases on Kaggle, HuggingFace, and GitHub.",
            expected_output="A list of clickable links to relevant datasets and tools for AI/ML use cases.",
            agent=agent,  # The agent responsible for performing this task
            output_file='Links.md'  # File where the output will be saved
        )

# Uncomment the following lines to test the PrepTask class
# if __name__ == "__main__":
#     task = PrepTask()
#     print(task.use_case_generation_task())
