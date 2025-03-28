from flask import Flask,request
from datetime import datetime

app = Flask(__name__)


#Global state variable 
state = "INIT"
run_log = []

@app.route("/state",methods=["GET","PUT"])
def handle_state():
    global state 
    if request.method == "GET":
        return state,200,{"Content-Type": "text/plain"}
    
    if request.method == "PUT":
        new_state = request.data.decode("utf-8")
        if new_state in ["INIT","PAUSED","RUNNING","SHUTDOWN"] and new_state != state:
            timestamp = datetime.utcnow().isoformat()
            run_log.append(f"{timestamp}: {state} -> {new_state}")
            state = new_state
            if new_state == "SHUTDOWN":
                pass


