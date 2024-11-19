from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()
import os

class SearchToolset():
    def tool():
        os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
        serperTool = SerperDevTool()
        #print(serperTool)
        return serperTool