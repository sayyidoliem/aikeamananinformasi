"""
Test Gemini API dengan berbagai model
"""
import requests
import json

api_key = "AIzaSyBlfHZNsvozZAezagCrB43uHz4KD7boByo"

# Coba beberapa model
models = [
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-pro"
]

test_prompt = "Halo, apa itu SQL Injection?"

print("="*70)
print("TESTING GEMINI API")
print("="*70)

for model in models:
    print(f"\n🧪 Testing model: {model}")
    print("-"*70)
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    data = {
        "contents": [{
            "parts": [{"text": test_prompt}]
        }]
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result:
                text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"✅ SUCCESS!")
                print(f"Response: {text[:150]}...")
                print(f"\n✨ MODEL YANG BEKERJA: {model}")
                break
        else:
            error = response.json().get('error', {})
            print(f"❌ Status: {response.status_code}")
            print(f"Error: {error.get('message', 'Unknown')[:100]}")
            
    except Exception as e:
        print(f"❌ Exception: {str(e)[:100]}")

print("\n" + "="*70)
