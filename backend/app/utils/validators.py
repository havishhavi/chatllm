import re

MAX_LENGTH = 1000  # Optional: Limit input to 1000 chars

def sanitize_input(message: str) -> str:
    if not message or not isinstance(message, str):
        return ""

    message = message.strip()
    if len(message) > MAX_LENGTH:
        message = message[:MAX_LENGTH]

    # Basic XSS protection
    message = re.sub(r"<[^>]+>", "", message)  # Remove HTML tags

    # Allow safe markdown symbols and code characters
    safe_message = re.sub(r"[^\w\s.,!?'\"]", "", message.strip())

    return safe_message
