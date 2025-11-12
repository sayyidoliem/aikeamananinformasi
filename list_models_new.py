import requests

api_key = "AIzaSyBlfHZNsvozZAezagCrB43uHz4KD7boByo"

# List all available models
response = requests.get(
    f'https://generativelanguage.googleapis.com/v1beta/models?key={api_key}',
    timeout=10
)

print(f"Status: {response.status_code}\n")

if response.status_code == 200:
    data = response.json()
    print("✅ Available models for generateContent:\n")
    
    for model in data.get('models', []):
        name = model.get('name', '')
        supported_methods = model.get('supportedGenerationMethods', [])
        
        if 'generateContent' in supported_methods:
            # Extract just the model name
            model_name = name.replace('models/', '')
            print(f"  ✓ {model_name}")
else:
    print(f"❌ Error: {response.text}")
