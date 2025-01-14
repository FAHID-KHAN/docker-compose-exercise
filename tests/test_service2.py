import requests

BASE_URL = "http://localhost:5000"

def test_service2_response():
    response = requests.get(f"{BASE_URL}/info")
    assert response.status_code == 200, "Service2 failed to respond correctly"

def test_service2_data():
    response = requests.get(f"{BASE_URL}/info")
    data = response.json()
    assert "uptime" in data, "Uptime missing from Service2 response"
    assert "processes" in data, "Processes missing from Service2 response"
