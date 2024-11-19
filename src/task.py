from crewai import Task

class PrepTask():
    def research_task(self, agent, tool):
        return Task(
            description="Use a web browser tool to research the company's industry, key offerings, and strategic focus.",
                expected_output="A detailed report of the company's industry, offerings, and strategic goals.",
                tools=[tool],
                agent=agent,
                async_execution=False
            )
        
    def use_case_generation_task(self, agent, tool):
        return Task(
                description="Analyze industry trends in AI/ML and automation and propose relevant use cases for the company.",
                expected_output="A list of relevant AI/ML use cases to improve company processes and customer experiences.",
                tools=[tool],
                agent=agent,
                output_file='new-blog-post.md',
                async_execution=False
            )


    def resource_collection_task(self, agent, tool):
        return Task(
                description="Search for relevant datasets for the proposed use cases on Kaggle, HuggingFace, and GitHub.",
                expected_output="A list of clickable links to relevant datasets and tools for AI/ML use cases.",
                agent=agent,
                output_file='Links.md'
            )