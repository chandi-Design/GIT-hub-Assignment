import requests

# This is the program to fetch your file from GitHub
url = "https://raw.githubusercontent.com/chandi-Design/Design-Portfolio/main/hello.py"

response = requests.get(url)

if response.status_code == 200:
    print("Success! File fetched from GitHub.")
    print("Content of hello.py:")
    print(response.text)
else:

    print("Failed to fetch file.")
