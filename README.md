# Agentic Cybersecurity Workflow

## Overview

This project is an **Agentic Cybersecurity Workflow** built using **LangGraph** and **LangChain**, integrated with the **Groq API**. The system automates cybersecurity tasks such as reconnaissance, scanning, and exploitation while providing a **Streamlit dashboard** for real-time monitoring.

## Features

- **Task Execution & Monitoring**: Automates security tasks using AI-driven workflows.
- **Scope Enforcement**: Ensures security tests remain within predefined boundaries.
- **Real-Time Logs**: Displays logs of each executed task.
- **Integration with Security Tools**:
  - **Nmap** (Network scanning)
  - **Gobuster** (Directory brute-force)
  - **FFUF** (Fuzzing tool)
  - **SQLmap** (SQL injection testing)
- **Streamlit Dashboard**: Provides a UI for managing scans and viewing results.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Virtual Environment (optional but recommended)
- Required dependencies from `requirements.txt`

### Steps

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/agentic-cybersecurity-workflow.git
   cd agentic-cybersecurity-workflow
   ```
2. **Create a Virtual Environment (Optional but Recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```
3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**:
   Create a `.env` file and add the necessary API keys:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```
5. **Run the Streamlit Dashboard**:
   ```sh
   streamlit run app.py
   ```

## Usage

1. Open the **Streamlit dashboard** in your browser.
2. Enter the target URL/IP.
3. Choose the security tool to execute.
4. View the logs and results in real-time.

## Project Structure

```
agentic-cybersecurity-workflow/
│── agent.py  # Main Streamlit application
│── requirements.txt
│── README.md
│── .env.example
```

## API Integration

This project utilizes the **Groq API** for task execution. Ensure you have a valid API key and configure it in `.env`.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Contributors

- **Prasanth Reddy** - [LinkedIn](https://www.linkedin.com/in/mannem-prasanthreddy-1a0a4a232/)

## Future Enhancements

- Integration with **AI-based threat detection**
- Support for **multi-agent collaboration**
- Enhanced **visual analytics**

## Contact

For queries or contributions, contact **Prasanth Reddy** at [[your.email@example.com](mailto\:your.email@example.com)] or connect on [LinkedIn](https://www.linkedin.com/in/mannem-prasanthreddy-1a0a4a232/).

