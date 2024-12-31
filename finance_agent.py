from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

## Web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

## Financial agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True, company_info=True, historical_prices=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
    add_datetime_to_instructions=True
)

if __name__=="__main__":
    # multi_ai_agent.print_response("what is stock price of apple today?", stream=True)
    from typing import Iterator

    # Run agent and return the response as a stream
    response_stream: Iterator[RunResponse] = multi_ai_agent.run("what is stock price of apple today?", stream=True)
    # Print the response stream in markdown format
    pprint_run_response(response_stream, markdown=True, show_time=True)


