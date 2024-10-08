from flask import Flask,jsonify
import requests
import os 
import subprocess

app = Flask(__name__)

def get_container_info():
    ip_address = os.popen("hostname -I || echo 'No IP'").read().strip()
    processes = os.popen("ps aux").read()
    disk_space = os.popen("df -h /").read()
    uptime_seconds = float(os.popen("cat /proc/uptime").read().split()[0])
    uptime_formatted = os.popen("uptime -p").read().strip()

    return {
        "ip_address": ip_address,
        "processes": processes,
        "disk_space": disk_space,
        "uptime_seconds":uptime_seconds,
        "uptime": uptime_formatted  # Use the formatted uptime here
    }

@app.route('/')
def index():
    #calling service 2
    try:
        service2_response = requests.get('http://service2:5000')
        service2_data = service2_response.json()
    except Exception as e:
        service2_data = {"error":str(e)}

    service1_data = get_container_info()
    return jsonify({
        "service1":service1_data,
        "service2": service2_data
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8199)