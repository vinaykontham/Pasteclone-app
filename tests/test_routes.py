# tests/test_routes.py
from fastapi.testclient import TestClient  # ✅ Correct import
from app.main import app

client = TestClient(app)

def test_create_snippet():
    response = client.post("/api/v1/snippets/", json={"content": "Hello World"})
    assert response.status_code == 200
    assert "link" in response.json()

def test_read_snippet():
    response = client.get("/api/v1/snippets/invalid_link")
    assert response.status_code == 404