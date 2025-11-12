"""
Direct API Test - Simple
"""
import requests

api_key = "AIzaSyBlfHZNsvozZAezagCrB43uHz4KD7boByo"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"

payload = {
    "contents": [{
        "parts": [{"text": "Hai"}]
    }]
}

print("Testing API...")
print(f"URL: {url[:100]}...")
print(f"Key: {api_key[:25]}...")
print()

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}")
print(f"\nFull Response:")
print(response.text)
