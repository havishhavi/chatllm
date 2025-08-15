from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_success():
    res = client.post("/chat", json={"message": "Hello"})
    assert res.status_code == 200
    assert "reply" in res.json()

def test_chat_empty():
    res = client.post("/chat", json={"message": ""})
    assert res.status_code == 422
