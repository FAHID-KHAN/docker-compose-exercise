import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Initial State
global_state = "INIT"
state_log = []
request_count = 0
start_time = datetime.now()

@app.route("/state", methods=["GET", "PUT"])
def state():
    global global_state
    global state_log

    if request.method == "GET":
        return global_state, 200, {"Content-Type": "text/plain"}

    if request.method == "PUT":
        new_state = request.data.decode("utf-8")
        if new_state in ["INIT", "PAUSED", "RUNNING", "SHUTDOWN"]:
            if new_state != global_state:
                state_log.append(f"{datetime.now()}: {global_state}->{new_state}")
                global_state = new_state

            # Special cases for INIT and SHUTDOWN
            if new_state == "INIT":
                global_state = "INIT"
                state_log.clear()
                return "State reset to INIT", 200

            if new_state == "SHUTDOWN":
               print("Shutting down services...")
               os.system("docker stop $(docker ps -q)")

            return f"State changed to {new_state}", 200
        else:
            return "Invalid state", 400

@app.route("/request", methods=["GET"])
def make_request():
    global request_count
    if global_state != "RUNNING":
        return "System is not in RUNNING state", 403

    # Simulate a request to Service1 (e.g., load balancer)
    request_count += 1
    return jsonify({"message": "Request processed", "total_requests": request_count})

@app.route("/run-log", methods=["GET"])
def run_log():
    return "\n".join(state_log), 200, {"Content-Type": "text/plain"}

@app.route("/monitor", methods=["GET"])
def monitor():
    uptime = datetime.now() - start_time
    return jsonify({
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime": str(uptime),
        "total_requests": request_count
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8197)
