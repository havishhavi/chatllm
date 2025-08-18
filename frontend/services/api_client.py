import requests
import uuid

API_URL = "http://localhost:8000/chat/"
_session_id = str(uuid.uuid4())

def get_llm_response(message: str, model: str, history: list, session_id: str) -> str:
    headers = {"X-Session-ID": session_id}
    payload = {
        "message": message,
        "model": model,
        "history": history
    }

    try:
        res = requests.post("http://localhost:8000/chat/", json=payload, headers=headers)

        if res.status_code == 429:
            raise Exception("⚠️ Rate limit exceeded. Please wait a few seconds and try again.")

        res.raise_for_status()
        return res.json()["reply"]

    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"❌ HTTP error: {http_err.response.text}")
    except Exception as err:
        raise Exception(f"❌ Unexpected error: {err}")
