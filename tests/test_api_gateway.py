import requests

BASE_URL = "http://localhost:8197"

def test_get_state():
    response = requests.get(f"{BASE_URL}/state")
    assert response.status_code == 200, "Failed to get state from API Gateway"
    assert response.text in ["INIT", "PAUSED", "RUNNING", "SHUTDOWN"], "Invalid state value"

def test_put_state():
    new_state = "RUNNING"
    response = requests.put(f"{BASE_URL}/state", data=new_state, headers={"Content-Type": "text/plain"})
    assert response.status_code == 200, "Failed to set state in API Gateway"
    response = requests.get(f"{BASE_URL}/state")
    assert response.text == new_state, "State was not updated correctly"

def test_run_log():
    response = requests.get(f"{BASE_URL}/run-log")
    assert response.status_code == 200, "Failed to retrieve run-log"
    assert "INIT->RUNNING" in response.text or "RUNNING->PAUSED" in response.text, "Run-log content is incorrect"
