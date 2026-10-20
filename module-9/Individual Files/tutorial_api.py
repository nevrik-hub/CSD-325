"""
Author: Nicholas Zankl
Date: 2026-08
Assignment: Module 9.2 Assignment - API Tutorial
Description: Program that tests API connectivity and parses JSON response 
             showing current astronauts in space.
"""

import requests

# 1. Test Connection
URL = "http://api.open-notify.org/astros.json"
response = requests.get(URL, timeout=10)

print("--- Step 1: Testing Connection ---")
print(f"Status Code: {response.status_code}")
print("-" * 35)

# 2. Retrieve and Format Astronaut Data
if response.status_code == 200:
    data = response.json()

    print("\n--- Current Astronauts in Space ---")
    print(f"Total People in Space: {data['number']}\n")

    # Loop through list of astronauts
    for person in data['people']:
        print(f"• {person['name']} (Craft: {person['craft']})")
else:
    print("Failed to retrieve data from API.")
