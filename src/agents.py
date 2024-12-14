from textwrap import dedent  # Utility for removing common leading whitespace from strings
from crewai import Agent  # Import the Agent class from CrewAI for defining agent behavior
from dotenv import load_dotenv  # For loading environment variables from a .env file
from tools import SearchToolset  # Import custom toolset for searching
from crewai_tools import SerperDevTool  # Import the SerperDevTool for web-based search functionalities

load_dotenv()  # Load environment variables from the .env file
from langchain_google_genai import ChatGoogleGenerativeAI  # Import ChatGoogleGenerativeAI for Google LLM integration
import os  # For handling environment variables and file system operations

import asyncio  # For asynchronous programming

# Set up the asyncio event loop (required for async operations)
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load environment variables (e.g., Google API key)
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the Google API key is set correctly
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set or invalid. Check your .env file.")

# Initialize the Language Model (LLM) using Google Generative AI
llm = ChatGoogleGenerativeAI(
    provider="google",  # Specify provider
    model="gemini-1.5-flash",  # Specify the model to use
    google_api_key=google_api_key,  # Provide the Google API key for authentication
    temperature=0.5,  # Set temperature for output variability (0.5 provides balanced responses)
    verbose=True  # Enable verbose logging for debugging purposes
)

# Define the PrepAgent class, which contains methods to initialize various agents
class PrepAgent():
    
    # Method to create an Industry Research Agent
    def Industry_Research_Agent(self):
        # Define an agent responsible for conducting industry research
        return Agent(
            role="Senior Researcher",  # The role of the agent
            goal=(
                "The agent's goal is to gather and analyze insights about the {topic} company's industry segment "
                "it is working in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare, etc.). "
                "Identify the company’s key offerings, and strategic focus areas (e.g., operations, supply chain, "
                "customer experience, etc.). A vision and product information on the industry should also be provided."
            ),
            verbose=False,  # Disable verbose output
            memory=True,  # Enable memory for agent's persistent context
            backstory=(
                "The agent was created to support market analysts working on identifying industry trends "
                "and evaluating potential partners, data, or competitors. Its role is to save time by "
                "automatically gathering and summarizing relevant data."
            ),
            tools=[SearchToolset.tool()],  # Assign tools for research tasks (e.g., web search)
            llm=llm,  # Assign the Google LLM for generating insights
            allow_delegation=False  # Disable delegation to other agents
        )
    
    # Method to create a Use Cases Generation Agent
    def Use_Cases_Generation(self):
        # Define an agent responsible for generating AI/ML use cases
        return Agent(
            role='Use Cases Generator',  # The role of the agent
            goal=(
                "The goal is to research industry standards, trends, and use cases for AI, ML, and automation "
                "in the specified sector. The agent identifies opportunities to leverage technologies like Generative AI, "
                "Large Language Models (LLMs), and other advanced ML tools, and recommends actionable strategies for improvement."
            ),
            verbose=False,  # Disable verbose output
            memory=True,  # Enable memory for agent's persistent context
            backstory=(
                "The agent is part of a strategic innovation initiative designed to help companies identify "
                "gaps and opportunities for leveraging advanced technologies like AI and LLMs. By generating "
                "detailed insights into industry practices and proposing relevant use cases, the agent supports "
                "decision-makers in staying competitive and enhancing operational excellence."
            ),
            # tools=[SearchToolset.tool()],  # Uncomment if additional tools are needed
            llm=llm,  # Assign the Google LLM for generating insights
            allow_delegation=False  # Disable delegation to other agents
        )
    
    # Method to create a Resource Asset Collection Agent
    def Resource_Asset_Collection(self):
        # Define an agent responsible for collecting resource assets
        return Agent(
            role="Research and Resource Collector",  # The role of the agent
            goal=(
                "Gather and organize datasets related to identified AI/ML use cases from Kaggle, HuggingFace, and GitHub. "
                "Propose GenAI solutions for enhanced workflows and save the resources in a structured markdown file."
            ),
            backstory=(
                "This agent supports AI innovation by streamlining the resource discovery process. It ensures that "
                "project teams can access the right datasets and tools quickly, enabling faster deployment of solutions. "
                "Additionally, it highlights opportunities for integrating GenAI to improve internal and customer-facing processes."
            ),
            # tools=[SearchToolset.tool()],  # Uncomment if additional tools are needed
            llm=llm,  # Assign the Google LLM for generating insights
            allow_delegation=False  # Disable delegation to other agents
        )

# Uncomment the following block to test the PrepAgent class
# if __name__ == "__main__":
#     # Initialize the PrepAgent class
#     prep_agent = PrepAgent()
#     
#     # Test the Industry_Research_Agent method
#     industry_research_agent = prep_agent.Industry_Research_Agent()
#     print(industry_research_agent)
