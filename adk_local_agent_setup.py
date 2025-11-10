#⚙️ 1. Install dependencies (run this once) 
"""
───────────────────────────────────────────────────────────────────────────────
🧠 GOOGLE AGENT DEVELOPMENT KIT (ADK) — LOCAL JUPYTER NOTEBOOK SETUP
───────────────────────────────────────────────────────────────────────────────
📄 Description:
This script demonstrates how to build and run a simple Google Agent Development
Kit (ADK) agent using the Gemini model, outside the Kaggle environment.

It configures your Gemini API key, imports ADK components, defines an agent,
creates a runner to manage conversations, and provides helper functions for
displaying the ADK Web UI and gracefully handling API quota errors.

📌 What This Script Does:
1️⃣ Installs and imports all required dependencies  
2️⃣ Configures your Gemini API Key (from Google AI Studio)  
3️⃣ Imports the Google ADK components  
4️⃣ Defines a custom AI agent powered by Gemini  
5️⃣ Creates an in-memory runner to process queries  
6️⃣ Provides helper functions for running and debugging the agent  
7️⃣ Displays a local or Kaggle-compatible ADK Web UI  
8️⃣ Handles API rate limits (HTTP 429) with retries  

───────────────────────────────────────────────────────────────────────────────
🚀 Author: Hari HaraSudhan
📅 Created: 2025-11-10  
🏷️ Repository: Hari / Google ADK Local Setup  
───────────────────────────────────────────────────────────────────────────────
"""

# ⚙️ 1. Install dependencies (only needed once)
# !pip install google-adk google-genai

# 🧩 2. Configure your Gemini API Key
import os

os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY_HERE"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

print("✅ Gemini API key setup complete.")


# 🧠 3. Import ADK Components
from IPython.display import display, HTML
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types

print("✅ ADK components imported successfully.")


# 🧩 4. Define your Agent
root_agent = Agent(
    name="helpful_assistant1",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

print("✅ Root Agent defined.")


# 🧠 5. Create the Runner
runner = InMemoryRunner(agent=root_agent)
print("✅ Runner created.")


# 🧰 6. Helper Functions
def _is_kaggle_env() -> bool:
    """Detect if running inside Kaggle."""
    return "KAGGLE_KERNEL_RUN_TYPE" in os.environ


def get_adk_ui_url(port: int = 8000) -> str:
    """
    Returns the correct ADK Web UI URL for local or Kaggle environments.
    - On Kaggle, builds the proxied URL for in-browser access.
    - Locally, defaults to http://localhost:8000.
    """
    try:
        from jupyter_server.serverapp import list_running_servers
    except Exception:
        list_running_servers = None

    if _is_kaggle_env() and list_running_servers:
        try:
            servers = list(list_running_servers())
            if not servers:
                return f"http://localhost:{port}"
            base_url = servers[0].get("base_url", "/")
            parts = [p for p in base_url.split("/") if p]
            if len(parts) >= 2:
                kernel = parts[1]
                token = parts[2] if len(parts) > 2 else ""
                url_prefix = f"/k/{kernel}/{token}/proxy/proxy/{port}"
                return f"https://kkb-production.jupyter-proxy.kaggle.net{url_prefix}"
        except Exception:
            pass
    return f"http://localhost:{port}"


def show_adk_button(port: int = 8000):
    """Display a clickable HTML button to open the ADK Web UI."""
    url = get_adk_ui_url(port)
    html = f"""
    <div style="padding:15px;border:2px solid #1a73e8;border-radius:8px;background:#f5f9ff;margin:20px 0;">
      <div style="font-family:sans-serif;margin-bottom:10px;color:#1a1a1a;font-size:1.05em;">
        <strong>ADK Web UI</strong>
      </div>
      <div style="font-family:sans-serif;margin-bottom:12px;color:#333;line-height:1.45;">
        Start the ADK web server (e.g. <code>!adk web --port {port}</code>), then click below:
      </div>
      <a href="{url}" target="_blank" style="
          display:inline-block;background:#1a73e8;color:#fff;padding:10px 16px;
          text-decoration:none;border-radius:24px;font-weight:600;">Open ADK Web UI ↗</a>
    </div>
    """
    display(HTML(html))


import asyncio


async def safe_run(prompt: str, retries: int = 2, backoff_seconds: int = 60):
    """
    Run the agent and automatically retry if a quota (429) error occurs.
    """
    last_error = None
    for attempt in range(1, retries + 2):
        try:
            return await runner.run_debug(prompt)
        except Exception as e:
            msg = str(e)
            last_error = e
            if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
                if attempt <= retries:
                    print(f"⚠️ Quota/rate limit hit. Retry {attempt}/{retries} in {backoff_seconds}s…")
                    await asyncio.sleep(backoff_seconds)
                    continue
            raise
    raise last_error or RuntimeError("Unknown error during safe_run")


async def ask(prompt: str):
    """
    Convenience wrapper to run prompts with nice output.
    """
    resp = await runner.run_debug(prompt)
    try:
        final = getattr(resp, "output_text", None)
        if final:
            print(final)
    except Exception:
        pass
    return resp


print("✅ Helper functions defined.")


# 🧭 7. Get your custom URL for ADK Web UI
url_prefix = get_adk_ui_url()
print(f"🌐 ADK Web UI available at: {url_prefix}")


# ⚙️ 8. Start ADK Web (run this manually in a notebook or terminal)
# !adk web --url_prefix {url_prefix}
