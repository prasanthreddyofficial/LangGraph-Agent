import os
import subprocess
import streamlit as st
import langgraph
import requests
from dotenv import load_dotenv
import langchain.globals as lc_globals

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Set LangChain verbosity
lc_globals.set_verbose(False)

# Define task execution functions
def get_wordlist_path():
    wordlist_path = os.path.join(os.getcwd(), "wordlist.txt")
    if not os.path.exists(wordlist_path):
        return None
    return wordlist_path

def run_command(command):
    try:
        process = subprocess.run(command, capture_output=True, text=True, shell=True)
        return process.stdout if process.returncode == 0 else f"Execution failed: {process.stderr}"
    except Exception as e:
        return f"Execution error: {e}"

def run_nmap(target):
    if not target:
        return "Error: No target specified."
    command = f"nmap -Pn -T4 -F {target}"  # Added -Pn to bypass ping check
    return run_command(command)

def run_gobuster(target):
    wordlist = get_wordlist_path()
    if "Error" in wordlist:
        return wordlist
    try:
        command = ["gobuster", "dir", "-u", target, "-w", wordlist]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Gobuster execution failed: {result.stderr}"
    except subprocess.CalledProcessError as e:
        return f"Gobuster execution failed: {e}"

def run_ffuf(target):
    wordlist = get_wordlist_path()
    if not wordlist:
        return "Error: Wordlist file not found."

    # Ensure target has http:// or https://
    if not target.startswith(("http://", "https://")):
        target = "http://" + target

    command = f"ffuf -u {target}/FUZZ -w {wordlist} -t 50 -mc 200,302,403,500"
    print(f"Executing FFUF: {command}")  # Debugging

    try:
        process = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = process.stdout.strip() or process.stderr.strip()
        return output if output else "FFUF execution returned no output."
    except Exception as e:
        return f"Execution error: {e}"


# Define LangGraph-based cybersecurity agent
def analyze_task(task):
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "llama3-8b-8192", "messages": [{"role": "user", "content": f"Break down this task: {task}"}], "temperature": 0.7}
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', 'No response content')
    else:
        return f"Error: {response.text}"

def main():
    st.title("LangGraph-Based Cybersecurity Agent")
    target = st.text_input("Enter Target (e.g., example.com)")
    
    if st.button("Analyze Task with AI"):
        ai_response = analyze_task(f"Scan {target} for vulnerabilities")
        st.text_area("AI Task Breakdown", ai_response, height=200)
    
    if st.button("Run Nmap Scan"):
        output = run_nmap(target)
        st.text_area("Nmap Output", output, height=300)
    
    if st.button("Run Gobuster Scan"):
        output = run_gobuster(target)
        st.text_area("Gobuster Output", output, height=300)
    
    if st.button("Run FFUF Scan"):
        output = run_ffuf(target)
        st.text_area("FFUF Output", output, height=300)

if __name__ == "__main__":
    main()
