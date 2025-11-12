import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')

# List all available models
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        print("=" * 70)
        print("AVAILABLE GEMINI MODELS:")
        print("=" * 70)
        
        if 'models' in data:
            for model in data['models']:
                name = model.get('name', 'N/A')
                display_name = model.get('displayName', 'N/A')
                methods = model.get('supportedGenerationMethods', [])
                
                if 'generateContent' in methods:
                    print(f"\n✅ Model: {name}")
                    print(f"   Display Name: {display_name}")
                    print(f"   Methods: {', '.join(methods)}")
        else:
            print("No models found")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
except Exception as e:
    print(f"Exception: {e}")
