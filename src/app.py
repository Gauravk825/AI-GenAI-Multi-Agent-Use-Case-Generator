import streamlit as st
import asyncio
from config import initialize_agents_and_tasks

# Configure the Streamlit app layout and title
st.set_page_config(layout="wide")
st.title('Multi-Agent Architecture for AI Use Case Generation and Industry Analysis')
st.subheader('Identify AI/ML Use Cases, Analyze Industry Trends, and Collect Relevant Resources')

# Sidebar for user input
with st.sidebar:
    st.title("Input Details")  # Sidebar title
    company_name = st.text_input("Company Name")  # Input field for the company name
    start_analysis = st.button("Generate Use Cases")  # Button to trigger the analysis process

# Asynchronous function to handle the analysis process
async def analyze_use_cases():
    try:
        # Initialize multi-agent architecture asynchronously
        crew = await initialize_agents_and_tasks()
        # Optional: Debug the initialized crew object
        # st.write("Initialized Crew:", crew)

        # Create input dictionary for agents to process
        inputs = {"topic": company_name}
        # Optional: Debug the input dictionary
        # st.write("Inputs:", inputs)

        # Check if the kickoff method is asynchronous and call it appropriately
        if asyncio.iscoroutinefunction(crew.kickoff):
            result = await crew.kickoff(inputs=inputs)  # Call asynchronously
        else:
            result = crew.kickoff(inputs=inputs)  # Call synchronously if not async

        # Optional: Debug the raw result returned from the kickoff process
        # st.write("Raw Kickoff Result:", result)

        # Handle string responses to wrap them for compatibility
        if isinstance(result, str):
            st.warning("Kickoff returned a string. Wrapping it for compatibility.")
            result = {"research_agent": {"result": result}}  # Convert string into a structured format

        # Process and display the results if they are structured as a dictionary
        if isinstance(result, dict):
            # Display industry research results
            st.subheader("Industry Research")
            st.write(result.get('research_agent', {}).get('result', "No data"))  # Default to "No data" if key is missing

            # Uncomment these sections to display other types of results if available
            # st.subheader("Generated Use Cases")
            # st.write(result.get('use_case_agent', {}).get('result', "No data"))

            # st.subheader("Resource Assets")
            # st.write(result.get('resorce_colletion', {}).get('result', "No data"))

            st.success("Analysis complete!")  # Show success message
        else:
            # Display an error if the result type is unexpected
            st.error(f"Unexpected result type: {type(result)}. Value: {result}")

    except Exception as e:
        # Display any exceptions that occur during execution
        st.error(f"An error occurred: {e}")

# Trigger the analysis process when the button is clicked
if start_analysis:
    asyncio.run(analyze_use_cases())  # Use asyncio to run the async function
