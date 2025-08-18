from dotenv import load_dotenv
import os

load_dotenv()

# --- Required for all providers ---
if not os.getenv("LLM_PROVIDER"):
    raise RuntimeError("Missing LLM_PROVIDER in environment.")

# --- OpenAI config ---
if os.getenv("LLM_PROVIDER").lower() == "openai":
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Missing OPENAI_API_KEY in environment.")

# --- Gemini config ---
if os.getenv("LLM_PROVIDER").lower() == "gemini":
    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("Missing GEMINI_API_KEY in environment.")

# --- Groq config ---
if os.getenv("LLM_PROVIDER").lower() == "grok":
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("Missing GROQ_API_KEY in environment.")
