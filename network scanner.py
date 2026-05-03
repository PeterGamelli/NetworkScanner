import subprocess
import socket
import jsonify
from flask import Flask

app = Flask(__name__)

@app.route("/")
def local_ip():
    return jsonify({"ip": get_local_ip()})

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

print(f"Local IP: {get_local_ip()}")



def check_ip_addr(addr_lst): 
    results = []
    for addr in addr_lst: 
        
        status, _ = subprocess.getstatusoutput(f'ping /n 1 {addr}')                     
        if status == 0: 
            results.append('yes')
        else: 
            results.append('no')
    return results

scan_results = check_ip_addr(input('Please enter IP addresses separated by commas: ').split(','))

print(scan_results)

