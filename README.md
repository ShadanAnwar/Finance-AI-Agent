# Multi-Agent AI App

This application leverages multiple AI agents powered by Groq's Llama models to provide intelligent responses for web search and financial insights. It integrates tool-specific capabilities like DuckDuckGo for web search and YFinance for financial data, all presented in an interactive Streamlit-based interface.

---

## Features

- **Web Search Agent**
  - Conducts detailed web searches using DuckDuckGo.
  - Displays results with sources included.

- **Finance AI Agent**
  - Provides financial data, including stock prices, analyst recommendations, company news, and more using YFinance tools.
  - Data is presented in a structured table format.

- **Multi-Agent System**
  - Combines the capabilities of Web Search Agent and Finance AI Agent.
  - Efficiently answers complex queries using a collaborative approach.

- **Streamlined Response Extraction**
  - Removes unnecessary system output and displays clean, meaningful responses.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/multi-agent-ai-app.git
   cd multi-agent-ai-app
   ```

2. **Set Up Environment**
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Create a `.env` file and add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key
     ```

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Select an Agent**
   - Choose between `Web Search Agent`, `Finance AI Agent`, or `Multi-Agent AI` from the sidebar.

2. **Enter Query**
   - Input your question or task in the text area provided.

3. **Get Response**
   - Click on `Get Response` and wait for the AI agent to process your query.

4. **View Results**
   - The clean and formatted response will appear in the main section of the app.

---

## How It Works

### Agent Framework
- **Web Search Agent**
  - Uses `DuckDuckGo` for web search queries.
  - Processes and displays search results with reference links.

- **Finance AI Agent**
  - Integrates YFinance tools to fetch stock-related data.
  - Utilizes tabular formatting for better readability.

- **Multi-Agent AI**
  - Combines the functionalities of both agents.
  - Allocates tasks dynamically to specialized agents for accurate results.

### Response Extraction
- A custom method processes raw agent output to:
  - Remove color codes, tool calls, and irrelevant lines.
  - Extract and display only the meaningful portion of the response.

---

## Dependencies

- **Python** >= 3.8
- **Libraries**:
  - `streamlit`
  - `dotenv`
  - `phi`
  - `yfinance`
  - `duckduckgo`

---

## Contributing

Contributions are welcome! If you'd like to improve or extend this app, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Create a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- **Groq AI** for providing powerful Llama models.
- **YFinance** for financial data insights.
- **DuckDuckGo** for web search capabilities.

---

### Contact

For questions or support, feel free to reach out at [shadan.anwar2005@gmail.com]([shadan.anwar2005@gmail.com).
