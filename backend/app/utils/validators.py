import re

def sanitize_input(message: str) -> str:
    if not message or not isinstance(message, str):
        return ""
    clean = re.sub(r"[^\w\s.,!?'\"]+", "", message.strip())
    return clean
