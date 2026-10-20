"""
Author: Nicholas Zankl
Date: 2026-08
Assignment: Module 9.2 Assignment - Custom API
Description: Connects to a custom public API, displays connection status, 
             unformatted response, and custom formatted output.
"""

import requests

# API Endpoint for a random joke
URL = "https://official-joke-api.appspot.com/random_joke"

print("====================================")
print("       Module 9.2: Custom API       ")
print("====================================\n")

# 1. Test Connection with a 10-second timeout
response = requests.get(URL, timeout=10)
print(f"1. Connection Status Code: {response.status_code}")

if response.status_code == 200:
    # 2. Print Unformatted Response (Raw JSON String)
    print("\n2. Unformatted (Raw JSON) Response:")
    print(response.text)

    # Parse JSON using requests built-in method
    data = response.json()

    # 3. Print Formatted Response
    print("\n3. Formatted Response:")
    print("-" * 35)
    print(f"Category : {data['type'].capitalize()}")
    print(f"Setup    : {data['setup']}")
    print(f"Punchline: {data['punchline']}")
    print("-" * 35)
else:
    print("Error fetching data from API.")
