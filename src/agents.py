from  textwrap import dedent
from crewai import Agent
from dotenv import load_dotenv
from tools import SearchToolset
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

class PrepAgent():
    def Industry_Research_Agent(self):
        #print(SearchToolset.tool())
        return Agent(
                role="Senior Researcher",
                goal="The agent's goal is to gather and analyze insights about {topic} company's industry segment, key offerings, and strategic focus to support strategic planning or competitive analysis.",
                verbose=True,
                memory=True,
                backstory=(
                    "The agent was created to support market analysts working on"
                    " identifying industry trends and evaluating potential partners"
                    "data or competitors in the automotive sector. Its role is to save" 
                    "time by automatically gathering and summarizing relevant data."

                ),
                tools=[SearchToolset.tool()],
                llm=llm,
                allow_delegation=True
                )
        
        
    def Use_Cases_Generation(self):
        return  Agent(
                role='Use Cases Generation',
                goal=("goal is to research industry standards, trends, and use cases for AI, ML, and automation" 
                        "in the specified sector, identify opportunities to leverage technologies like Generative AI, Large"
                        "Language Models (LLMs), and other advanced ML tools, and recommend actionable strategies for improvement."),
                verbose=True,
                memory=True,
                backstory=(
                    "The agent is part of a strategic innovation initiative designed to help companies "
                    "identify gaps and opportunities for leveraging advanced technologies like AI and LLMs."
                    "By generating detailed insights into industry practices and proposing relevant use "
                    "cases, the agent supports decision-makers in staying competitive and enhancing operational excellence."
                ),
                tools=[SearchToolset.tool()],
                llm=llm,
                allow_delegation=True
                )
        
    def Resource_Asset_Collection(self):
        return Agent(
                role="Research and Resource Collector",
                goal="Gather and organize datasets related to identified AI/ML use cases from Kaggle, HuggingFace, and GitHub. Propose GenAI solutions for enhanced workflows and save the resources in a structured markdown file.",
                backstory="This agent supports AI innovation by streamlining the resource discovery process. It ensures that project teams can access the right datasets and tools quickly, enabling faster deployment of solutions. Additionally, it highlights opportunities for integrating GenAI to improve internal and customer-facing processes.",
                #tools=[SearchToolset.tool()],
                llm=llm,
                allow_delegation=False
                )