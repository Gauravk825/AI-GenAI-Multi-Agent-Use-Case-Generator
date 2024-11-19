from crewai import Crew,Process
from task import PrepTask
from agents import PrepAgent
from tools import SearchToolset


def main():
    
    print("Welocme")
    task = PrepTask()
    agents  = PrepAgent()
    #topic = input("Enter industry name : ")
    # Create agents 
    tool = SearchToolset.tool()
    research_agent = agents.Industry_Research_Agent()
    use_case_agent = agents.Use_Cases_Generation()
    resorce_colletion = agents.Resource_Asset_Collection()
    
    # Creating Task
    research_task = task.research_task(research_agent, tool)
    use_case_task = task.use_case_generation_task(use_case_agent, tool)
    resorce_link = task.research_task(resorce_colletion, tool)
    
    crew = Crew(
        agents=[research_agent, use_case_agent, resorce_colletion],
        tasks=[research_task, use_case_task, resorce_link],
        process=Process.sequential
        )
    
    result = crew.kickoff(inputs={'topic':'Crewai'})
    print(result)
    
if __name__ == "__main__":
    main()