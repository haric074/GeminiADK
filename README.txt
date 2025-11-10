🧠 Google Agent Development Kit (ADK) – Local Jupyter Setup
⚙️ Overview

This project demonstrates how to set up and run the Google Agent Development Kit (ADK) locally using the Gemini 2.5 Flash model, outside the Kaggle environment.

You’ll learn how to configure your Gemini API key, define a custom agent, run queries using Google Search, and even launch the ADK Web UI from your Jupyter environment.

✨ Features

✅ Build a fully functional AI Agent using Google’s Gemini model
✅ Works locally or on Kaggle
✅ Includes helper functions to handle web UI, retries, and environment detection
✅ Handles API rate limits (429 errors) gracefully
✅ Launch the ADK Web UI interactively with one click
✅ Built with Python + AsyncIO for modern, clean design

🧰 Requirements

You’ll need:

Python 3.9 or later

Jupyter Notebook or JupyterLab

A valid Gemini API Key (get it from Google AI Studio
)

📦 Installation
1️⃣ Clone this repository
git clone https://github.com/<your-username>/google-adk-local-setup.git
cd google-adk-local-setup

2️⃣ Install dependencies
pip install google-adk google-genai

🔑 3️⃣ Configure your Gemini API Key

Open adk_local_agent_setup.py and replace the placeholder with your API key:

os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

🧩 4️⃣ Define Your Agent

This setup creates a simple but powerful Gemini-based agent that can answer general questions and perform Google Search when needed.

root_agent = Agent(
    name="helpful_assistant1",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

🧠 5️⃣ Create and Run the Agent
Create the runner:
runner = InMemoryRunner(agent=root_agent)
print("✅ Runner created.")

Run your first prompt:
import asyncio
await runner.run_debug("What is Agent Development Kit from Google?")

🧰 6️⃣ Helper Functions

Includes:

✅ show_adk_button() – Displays a clickable button to open the ADK Web UI

✅ safe_run(prompt) – Automatically retries if rate limit (429) is hit

✅ ask(prompt) – Clean wrapper for quick prompts

await ask("What's the weather in London?")

🌐 7️⃣ Launch ADK Web UI (optional)
Start the web UI server:
adk web --port 8000

Then, in your Jupyter Notebook:
show_adk_button(port=8000)


A clickable button will appear to open your agent UI directly in the browser.
If you’re using Kaggle, it will auto-generate a proxied Kaggle URL.

🪄 Example Output

Input:

await ask("What is Agent Development Kit from Google?")


Output:

The Agent Development Kit (ADK) is a framework from Google that helps developers
build, test, and deploy AI agents using Gemini models. It supports Python and JavaScript
SDKs and integrates with tools like Google Search, Vertex AI, and custom APIs.

📁 Project Structure
📦 google-adk-local-setup/
 ┣ 📜 adk_local_agent_setup.py    # Main setup and agent script
 ┣ 📜 README.md                   # This documentation
 ┗ 📜 requirements.txt            # Optional dependency list

🧩 Tech Stack
Component	Description
🐍 Python	Core programming language
🤖 Google ADK	Framework for building AI agents
🌐 Gemini API	Underlying LLM used by the agent
🔍 google-search tool	Provides real-time web data
🧪 AsyncIO	For async query execution and retries
💻 Jupyter	Interactive development environment
🏆 Personal Note – My Achievement

🎯 What I Achieved

I successfully configured and ran Google’s Agent Development Kit (ADK) locally — outside the Kaggle/Colab ecosystem.
This setup uses Gemini 2.5 Flash with Google Search integration, allowing real-time information retrieval and natural conversations.

💡 I created helper utilities to:

Detect if running locally or in Kaggle

Launch the ADK Web UI with one click

Handle rate-limit errors gracefully (HTTP 429)

🔧 Tech Used: Python, Google ADK, Gemini API, AsyncIO, Jupyter

🚀 Finally worked after multiple trials and debugging — now shared to help others set up ADK locally with zero friction!

🧑‍💻 Author

👤 Hari
🪟 Hari’s Window – Exploring technology, travel, and AI innovations.
📧 Reach me: [your.email@example.com
]
🌐 YouTube: Hari’s Window

⭐ Contribute

Feel free to fork this repo, improve it, and send pull requests!
If this project helped you, please consider starring ⭐ it on GitHub.

📜 License

This project is licensed under the MIT License — free to use, modify, and distribute.

🔗 Quick Links
Resource	URL
🧠 Google AI Studio	https://makersuite.google.com/app/apikey

📚 ADK Documentation	https://cloud.google.com/agent-development-kit/docs

💬 Gemini API Docs	https://ai.google.dev/docs
