import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = "AIzaSyBlfHZNsvozZAezagCrB43uHz4KD7boByo"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"

headers = {'Content-Type': 'application/json'}

data = {
    "contents": [{
        "parts": [{
            "text": "Halo, apa itu keamanan informasi?"
        }]
    }],
    "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 2048,
    }
}

print("Testing Gemini API...")
print(f"URL: {url[:80]}...")
print(f"API Key: {api_key[:20]}...")
print("\nSending request...\n")

try:
    response = requests.post(url, headers=headers, json=data, timeout=30)
    
    print(f"Status Code: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2))
    
    if response.status_code == 200:
        result = response.json()
        if 'candidates' in result:
            text = result['candidates'][0]['content']['parts'][0]['text']
            print(f"\n✅ SUCCESS! AI Response:\n{text}")
    else:
        print(f"\n❌ ERROR!")
        
except Exception as e:
    print(f"Exception: {e}")
