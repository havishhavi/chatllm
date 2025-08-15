from dotenv import load_dotenv
import os

load_dotenv()

# Optional: validate presence of critical variables
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("Missing OPENAI_API_KEY in environment.")
