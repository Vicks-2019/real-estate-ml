from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_prediction():
    response = client.post("/predict", json={
        "unit_area": 1200,
        "total_rooms": 3,
        "bathrooms": 2
    })
    assert response.status_code == 200