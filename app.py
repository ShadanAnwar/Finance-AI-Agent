import streamlit as st
from helper_func import ResearchAgent, process_research_response
from finance_agent import finance_agent, web_search_agent, multi_ai_agent

# Initialize agents
research_agents = {
    "General Research": multi_ai_agent,
    "Financial Research": finance_agent,
    "Web Search": web_search_agent
}

# Wrap agents with research capabilities
research_agents = {name: ResearchAgent(**agent.__dict__) 
                  for name, agent in research_agents.items()}

# Streamlit app
st.title("AI Research Assistant")
st.write("Ask any research question - from market data to general knowledge.")

# Sidebar for agent selection
st.sidebar.header("Research Mode")
agent_option = st.sidebar.selectbox(
    "Choose your research mode:",
    list(research_agents.keys())
)

# Query input
st.sidebar.header("Research Query")
user_query = st.sidebar.text_area(
    "What would you like to research?",
    placeholder="Enter your question here...",
    height=100
)

# Process button
if st.sidebar.button("Research", type="primary"):
    with st.spinner("Researching your query..."):
        try:
            # Get response stream from selected agent
            selected_agent = research_agents[agent_option]
            response_stream = selected_agent.get_response(user_query)

            # Process and clean the response
            clean_response_text = process_research_response(response_stream)

            # Display results
            st.markdown("### Research Results")
            if clean_response_text.strip():
                st.markdown(clean_response_text)
            else:
                st.warning("Could not find meaningful results. Please try rephrasing your query.")

        except Exception as e:
            st.error(f"Research error: {str(e)}")
            st.error("Please try again or rephrase your query.")

# Information section
st.sidebar.markdown("---")
st.sidebar.header("About")
st.sidebar.info(
    """
    This AI Research Assistant can help you with:
    - General knowledge queries
    - Financial research and market data
    - Web searches and current information
    - Data analysis and insights
    """
)

