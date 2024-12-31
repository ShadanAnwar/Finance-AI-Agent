from phi.agent import Agent, RunResponse
from typing import Iterator
import re

class ResearchAgent(Agent):
    def get_response(self, query):
        return self.run(query, stream=True)

def process_research_response(response_stream: Iterator[RunResponse]) -> str:
    """Process and clean the research response from a RunResponse stream"""
    full_response = ""
    for response in response_stream:
        if response.content:
            full_response += response.content

    # Clean the full response
    cleaned = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', full_response)  # Remove ANSI color codes
    cleaned = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned)  # Remove control characters
    cleaned = re.sub(r'[┏┓┗┛━┃]', '', cleaned)  # Remove box drawing characters
    cleaned = re.sub(r'Message|Response $$\d+\.\d+s$$', '', cleaned)  # Remove system messages
    cleaned = re.sub(r'Running:.*?additional_information=.*?\)', '', cleaned, flags=re.DOTALL)  # Remove running messages

    # Extract the main content (assuming it's after the last occurrence of "Response")
    main_content = re.split(r'Response $$\d+\.\d+s$$', cleaned)[-1].strip()

    # Remove extra whitespace and newlines
    main_content = re.sub(r'\s+', ' ', main_content).strip()

    # Ensure proper capitalization
    if main_content and main_content[0].isalpha():
        main_content = main_content[0].upper() + main_content[1:]

    return main_content if main_content else "No meaningful information could be extracted from the response."

