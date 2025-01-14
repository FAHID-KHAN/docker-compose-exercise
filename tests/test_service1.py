import requests

BASE_URL = "http://localhost:8199"

def test_service1_response():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200, "Service1 failed to respond correctly"

def test_service1_data():
    response = requests.get(f"{BASE_URL}/")
    data = response.json()
    assert "ip_address" in data, "IP Address missing from Service1 response"
    assert "disk_space" in data, "Disk Space missing from Service1 response"
