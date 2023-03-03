# import requests
# import time
# import subprocess
#
# # The path of your server script
# server_path = "server.py"
#
# # The url of your api endpoint
# api_url = "http://localhost:8000"
#
# # A flag to indicate if the server is running or not
# server_running = True
#
# # A loop that runs until you stop the script
# while True:
#     # Create a child process that runs your server script
#     server_process = subprocess.Popen(["python", server_path])
#
#     # Wait for some time before checking the status of the api
#     time.sleep(10)
#
#     # Make a GET request to your api endpoint
#     response = requests.get(api_url)
#
#     # Check if the status code is 200, which means OK
#     if response.status_code == 200:
#         print("API is working fine.")
#
#     # If the status code is not 200, it means something went wrong
#     else:
#         print(f"API has failed with status code {response.status_code}.")
#         print("Restarting the server...")
#         # Set the flag to False to indicate that the server is not running
#         server_running = False
#
#     # If the flag is False, it means we need to restart the server
#     if not server_running:
#         # Terminate any remaining processes related to your server script
#         subprocess.run(["pkill", "-f", server_path])
#         # Set the flag back to True to indicate that we are restarting the server
#         server_running = True
#
#     # Wait for 5 seconds before making another request
#     time.sleep(5)

import requests
import time
import subprocess

# The path of your server script
server_path = "server.py"

# The url of your api endpoint
api_url = "http://localhost:8000"

# A flag to indicate if the server is running or not
server_running = True

# A loop that runs until you stop the script
while True:
    # Create a child process that runs your server script
    server_process = subprocess.Popen(["python", server_path])

    # Wait for some time before checking the status of the api
    time.sleep(10)

    # Try to make a GET request to your api endpoint with a 2 second timeout
    try:
        response = requests.get(api_url, timeout=2)

        # Check if the status code is 200, which means OK
        if response.status_code == 200:
            print("API is working fine.")

        # If the status code is not 200, it means something went wrong
        else:
            print(f"API has failed with status code {response.status_code}.")
            print("Restarting the server...")
            # Set the flag to False to indicate that the server is not running
            server_running = False

    # If there is a timeout exception, it means no response from the api
    except requests.exceptions.Timeout:
        print("API has timed out.")
        print("Restarting the server...")
        # Set the flag to False to indicate that the server is not running
        server_running = False

    # If there is any other exception, it means an unexpected error occurred
    except Exception as e:
        print(f"An error occurred: {e}")

    # If the flag is False, it means we need to restart the server
    if not server_running:
        # Terminate any remaining processes related to your server script
        subprocess.run(["pkill", "-f", server_path])
        # Set the flag back to True to indicate that we are restarting the server
        server_running = True

    # Wait for 5 seconds before making another request
    time.sleep(5)