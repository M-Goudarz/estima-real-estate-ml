from fastapi.testclient import TestClient

from estima.api import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_price():
    payload = {
        "Area": 100,
        "Room": 2,
        "Parking": True,
        "Warehouse": True,
        "Elevator": True,
        "Address": "Shahran",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "predicted_price_toman" in response.json()
    assert response.json()["predicted_price_toman"] > 0


def test_predict_invalid_area():
    payload = {
        "Area": -10,
        "Room": 2,
        "Parking": True,
        "Warehouse": True,
        "Elevator": True,
        "Address": "Shahran",
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422