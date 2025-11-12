import requests
import json

api_key = "AIzaSyBlfHZNsvozZAezagCrB43uHz4KD7boByo"

models_to_test = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-latest"
]

prompt = "Apa perbedaan antara virus, malware, dan ransomware?"

print("Testing API dengan prompt keamanan...\n")

for model in models_to_test:
    print(f"🔍 Testing: {model}")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 500
        }
    }
    
    try:
        response = requests.post(url, json=data, timeout=5)
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            text = result['candidates'][0]['content']['parts'][0]['text']
            print(f"   ✅ SUCCESS!")
            print(f"   Response: {text[:150]}...")
            print(f"\n✅ MODEL YANG BEKERJA: {model}\n")
            break
        else:
            error = response.json()
            error_msg = error.get('error', {}).get('message', 'Unknown')
            print(f"   ❌ Error: {error_msg[:100]}")
            
    except requests.exceptions.Timeout:
        print(f"   ⏱️ Timeout after 5 seconds")
    except Exception as e:
        print(f"   ❌ Exception: {str(e)[:100]}")
    
    print()
