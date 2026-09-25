#!/usr/bin/env python3
"""
Debug script to find the correct Aviapages API endpoint
"""

import httpx
import os

TOKEN = os.getenv("AVIAPAGES_API_TOKEN", "qOAgJCLM8SJTnPQZxF2SOqW5hiZofySiU4KF")

# Common API base URLs to try
urls_to_try = [
    "https://api.aviapages.com/api/v2",
    "https://api.aviapages.com/v2",
    "https://api.aviapages.com/v1",
    "https://api.aviapages.com",
    "https://aviapages.com/api/v2",
    "https://app.aviapages.com/api/v2",
]

print("🔍 Testing Aviapages API endpoints...\n")

for base_url in urls_to_try:
    print(f"Trying: {base_url}")

    try:
        response = httpx.get(
            f"{base_url}/airports",
            headers={"Authorization": f"Bearer {TOKEN}"},
            timeout=5,
        )

        print(f"  Status: {response.status_code}")

        if response.status_code == 200:
            print(f"  ✅ SUCCESS! Use: {base_url}")
            print(f"  Response: {response.json()[:100]}")
            break
        elif response.status_code in [401, 403]:
            print(f"  ⚠️  Auth issue (token might be wrong)")
        elif response.status_code == 404:
            print(f"  ❌ Not found (wrong endpoint)")
        else:
            print(f"  ⚠️  Status code: {response.status_code}")

    except Exception as e:
        print(f"  ❌ Error: {e}")

    print()

print("\nAlternative: Check Aviapages dashboard for API docs")
print("- Login to https://aviapages.com")
print("- Look for API documentation or settings")
print("- Find the correct endpoint URL")
