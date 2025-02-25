# LangGraph Cybersecurity Agent

## Overview

This project helps you check websites and networks for security issues. It:
1. Breaks down a security instruction into smaller, manageable tasks.
2. Creates a list of tasks and runs them one by one.
3. Ensures tasks are only run on allowed websites or IP addresses.
4. Uses tools like nmap, Gobuster, ffuf, and sqlmap to find security problems.
5. Updates the task list based on what it finds.
6. Logs everything it does and creates a final report.
7. Provides an easy-to-use dashboard to manage and view tasks.

## Features

- **Task Breakdown**: Turns high-level security instructions into detailed tasks.
- **Scope Management**: Ensures tasks are run only on allowed websites/IPs.
- **Fast Nmap Scans**: Uses quick settings for fast scans.
- **Dynamic Task Management**: Updates task list based on scan results.
- **Logging and Reporting**: Logs all actions and generates a final report.
- **Dashboard**: Simple interface for managing and viewing tasks.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/langchain-llm-app.git
    cd langchain-llm-app
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a `.env` file in the project root and add your GROQ API key:
    ```
    GROQ_API_KEY=your_groq_api_key
    ```

4. **Run the Streamlit app**:
    ```sh
    streamlit run /d:/langchain-llm-app/LangGraph-CyberSecurity/agent.py
    ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter allowed websites and IP addresses in the sidebar.
3. Provide a high-level security instruction.
4. Generate the task list and run all tasks.
5. View task logs and generate the final report.


