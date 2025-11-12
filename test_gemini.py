"""
Test Gemini API Connection
"""
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 Testing Gemini API Connection...")
print("=" * 60)

try:
    # Configure API
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY tidak ditemukan di .env")
        exit(1)
    
    genai.configure(api_key=api_key)
    print(f"✅ API Key configured: {api_key[:20]}...")
    
    # Test dengan model yang benar
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    print("✅ Model created: models/gemini-1.5-flash")
    
    # Test generate
    response = model.generate_content("Jelaskan singkat apa itu keamanan informasi dalam 2 kalimat.")
    print("\n📝 Test Response:")
    print("-" * 60)
    print(response.text)
    print("-" * 60)
    print("\n✅ Gemini API working perfectly!")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTrying to list available models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"  ✓ {m.name}")
    except Exception as e2:
        print(f"Cannot list models: {e2}")
