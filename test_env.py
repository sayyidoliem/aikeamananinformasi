"""
Quick test untuk memastikan API key terbaca dengan benar
"""
import os
from dotenv import load_dotenv

# Force reload .env
load_dotenv(override=True)

api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key dari .env: {api_key}")
print(f"Panjang: {len(api_key) if api_key else 0} karakter")
print(f"Preview: {api_key[:20] if api_key else 'N/A'}...")
