from dotenv import load_dotenv  # For loading environment variables from a .env file
from crewai_tools import SerperDevTool  # Importing the SerperDevTool for search functionality
load_dotenv()  # Automatically loads variables from a .env file
import os  # For interacting with the operating system's environment variables

class SearchToolset():
    """
    A utility class to configure and return a search tool object (SerperDevTool) for use in CrewAI tasks.
    The API key is securely retrieved from the environment variables using python-dotenv.
    """

    def tool():
        """
        Static method to configure the SerperDevTool with the API key and return the tool instance.

        Returns:
            serperTool (SerperDevTool): Configured instance of the SerperDevTool.
        """
        # Retrieve the API key from environment variables
        os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

        # Initialize the SerperDevTool using the retrieved API key
        serperTool = SerperDevTool()

        # Return the configured search tool
        return serperTool

# Uncomment the following lines to test the SearchToolset class functionality
# if __name__ == "__main__":
#      tool = SearchToolset.tool()
#      print(tool)
