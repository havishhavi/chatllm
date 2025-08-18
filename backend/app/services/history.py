import os
import json
from datetime import datetime
from typing import List, Dict

HISTORY_DIR = os.path.join(os.path.dirname(__file__), "..", "history")
os.makedirs(HISTORY_DIR, exist_ok=True)

def get_history_path(session_id: str) -> str:
    return os.path.join(HISTORY_DIR, f"{session_id}.json")

def save_to_history(session_id: str, message: Dict[str, str]):
    path = get_history_path(session_id)
    history = load_history(session_id)
    history.append(message)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def load_history(session_id: str) -> List[Dict[str, str]]:
    path = get_history_path(session_id)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def list_all_histories() -> List[str]:
    return [f for f in os.listdir(HISTORY_DIR) if f.endswith(".json")]
