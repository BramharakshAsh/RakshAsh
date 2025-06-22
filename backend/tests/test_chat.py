from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_endpoint():
    response = client.post("/api/chat", json={"prompt": "Hello"})
    assert response.status_code == 200
    assert "reply" in response.json()
