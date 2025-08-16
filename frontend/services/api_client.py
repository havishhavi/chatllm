import requests

API_URL = "http://localhost:8000/chat/"

def get_llm_response(message: str, model: str, history: list) -> str:
    payload = {
        "message": message,
        "model": model,
        "history": history
    }
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()["reply"]
