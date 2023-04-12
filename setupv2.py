import subprocess
import time
import os
import signal
import http.client

# function to send a get request to a host and return True if status 200, False otherwise
def get_request(host):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", "/")
    response = connection.getresponse()
    return response.status == 200

# function to run server.py as a subprocess and return its pid
def run_server():
    process = subprocess.Popen(["python", "server.py"])
    return process.pid

# function to kill a process by its pid
def kill_server(pid):
    os.kill(pid, signal.SIGTERM)

# run server.py for the first time and get its pid
server_pid = run_server()

# loop forever
while True:
    # send a get request to localhost:8000 and check the response
    response = get_request("localhost:8000")
    # if response is False, kill the current server and run a new one
    if not response:
        kill_server(server_pid)
        server_pid = run_server()
        print("Server restarted.")
    # wait for 5 seconds before sending another request
    time.sleep(5)