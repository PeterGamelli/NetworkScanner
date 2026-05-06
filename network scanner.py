import subprocess
import socket
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/local-ip")
def local_ip():
    return jsonify({"ip": get_local_ip()})

@app.route("/api/ip-input", methods=["POST"])
def ipinput():
    data = request.get_json()
    ip = data.get("ip")
    result = check_ip_addr([ip])

    return jsonify({"alive": result[0]})

def check_ip_addr(addr_lst):
    results = []
    for addr in addr_lst:
        completed = subprocess.run(
            ["ping", "/n", "1", addr],
            capture_output=True,
            text=True,
            check=False,
        )
        results.append(completed.returncode == 0)
    return results

if __name__ == "__main__":
    app.run(debug=True)
