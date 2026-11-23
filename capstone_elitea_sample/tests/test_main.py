from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_list_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_existing_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Wireless Mouse"

def test_get_missing_product():
    response = client.get("/products/999")
    assert response.status_code == 404
