import pytest

valid_payload = {
    "message": "Hello!",
    "model": "openai",
    "history": []
}

@pytest.mark.parametrize("model", ["openai", "gemini", "grok"])
def test_chat_success(client, model):
    payload = valid_payload.copy()
    payload["model"] = model
    res = client.post("/chat", json=payload)
    assert res.status_code == 200
    assert "reply" in res.json()
    assert isinstance(res.json()["reply"], str)

def test_chat_empty_message(client):
    payload = valid_payload.copy()
    payload["message"] = ""
    res = client.post("/chat", json=payload)
    assert res.status_code == 422

def test_chat_missing_model(client):
    payload = valid_payload.copy()
    payload.pop("model")
    res = client.post("/chat", json=payload)
    assert res.status_code == 422

def test_chat_invalid_model(client):
    payload = valid_payload.copy()
    payload["model"] = "invalid_model"
    res = client.post("/chat", json=payload)
    assert res.status_code == 500
    assert "Unsupported LLM provider" in res.text

def test_chat_with_history(client):
    payload = {
        "message": "What is your name?",
        "model": "openai",
        "history": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
    }
    res = client.post("/chat", json=payload)
    assert res.status_code == 200
    assert "reply" in res.json()
    assert isinstance(res.json()["reply"], str)