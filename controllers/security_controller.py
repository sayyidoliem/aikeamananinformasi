import google.generativeai as genai
from config import Config
from models.security_model import SecurityModel
import re
import requests
import json

class SecurityController:
    """Controller untuk menangani logika keamanan informasi"""
    
    def __init__(self):
        self.model_data = SecurityModel()
        self.setup_gemini()
    
    def clean_ai_response(self, text):
        """Clean AI response from markdown formatting"""
        import re
        
        # Remove markdown bold/italic
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)  # bold+italic
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)      # bold
        text = re.sub(r'\*(.+?)\*', r'\1', text)          # italic
        
        # Remove markdown headers
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
        
        # Clean up markdown tables
        text = re.sub(r'\|.*?\|', '', text)  # Remove table content
        text = re.sub(r'[:\-\|]{3,}', '', text)  # Remove table separators
        
        # Remove excessive newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Remove markdown code blocks
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        
        return text.strip()
        
    def setup_gemini(self):
        """Setup Gemini AI using REST API"""
        try:
            self.api_key = Config.GEMINI_API_KEY
            
            # Gunakan gemini-2.0-flash yang TESTED WORKS!
            self.model_urls = [
                ("gemini-2.0-flash", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"),
                ("gemini-flash-latest", "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"),
            ]
            
            # Default ke yang pertama
            self.current_model = self.model_urls[0][0]
            self.api_url = self.model_urls[0][1]
            
            if self.api_key:
                self.ai_available = True
                print(f"✅ Gemini AI configured with model: {self.current_model}")
            else:
                self.ai_available = False
                print("❌ Gemini API Key tidak ditemukan")
                
        except Exception as e:
            print(f"❌ Error setting up Gemini: {e}")
            self.ai_available = False
    
    def call_gemini_api(self, prompt, max_retries=1):
        """Call Gemini API directly using REST - try multiple models"""
        import time
        
        # Try each model until one works
        for model_name, model_url in self.model_urls:
            try:
                url = f"{model_url}?key={self.api_key}"
                
                headers = {
                    'Content-Type': 'application/json'
                }
                
                # Format yang benar untuk Gemini API - optimized for speed
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
                
                print(f"🔍 Trying model: {model_name}...")
                
                response = requests.post(url, headers=headers, json=data, timeout=5)
                
                print(f"📊 Status: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json()
                    if 'candidates' in result and len(result['candidates']) > 0:
                        text = result['candidates'][0]['content']['parts'][0]['text']
                        print(f"✅ Success with model: {model_name}")
                        # Cache working model
                        self.api_url = model_url
                        self.current_model = model_name
                        # Clean formatting
                        cleaned_text = self.clean_ai_response(text)
                        return cleaned_text
                    else:
                        continue  # Try next model
                        
                elif response.status_code == 429:
                    # Rate limit - try next model
                    print(f"⚠️ {model_name} rate limited, trying next...")
                    continue
                else:
                    # Other errors - try next model
                    try:
                        error_data = response.json()
                        error_msg = error_data.get('error', {}).get('message', 'Unknown error')
                        print(f"❌ {model_name}: {error_msg[:80]}")
                        continue  # Try next model
                    except:
                        continue
                        
            except requests.exceptions.Timeout:
                print(f"⏱️ {model_name} timeout, trying next...")
                continue
                
            except Exception as e:
                print(f"❌ {model_name} error: {str(e)[:50]}")
                continue
        
        # All models failed
        return """❌ Semua model Gemini tidak tersedia

Kemungkinan penyebab:
- Quota API habis untuk semua model
- API key belum aktif sepenuhnya

Solusi:
1. Tunggu 1-2 menit, lalu refresh halaman
2. Gunakan API key baru: https://makersuite.google.com/app/apikey
3. Atau gunakan fitur tanpa AI:
   ✓ Enkripsi/Dekripsi
   ✓ Check Password Strength
   ✓ Quick Vulnerability Scan"""
    
    def analyze_security_threat(self, text):
        """Analyze potential security threats in text"""
        if not self.ai_available:
            return {
                'success': False,
                'error': 'AI service tidak tersedia'
            }
        
        try:
            prompt = f"""
            Sebagai ahli keamanan informasi, analisis teks berikut untuk potensi ancaman keamanan:
            
            Teks: "{text}"
            
            PENTING: Jawab dalam format PLAIN TEXT (tanpa *, **, #, |, atau ```).
            
            TINGKAT ANCAMAN: [Rendah/Sedang/Tinggi/Kritis]
            
            JENIS ANCAMAN:
            [Sebutkan jenis ancaman]
            
            DESKRIPSI:
            [Penjelasan singkat 2-3 kalimat]
            
            REKOMENDASI:
            - [Rekomendasi 1]
            - [Rekomendasi 2]
            - [Rekomendasi 3]
            
            Bahasa Indonesia. Maksimal 250 kata.
            """
            
            analysis_text = self.call_gemini_api(prompt)
            
            return {
                'success': True,
                'analysis': analysis_text,
                'input': text
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def encrypt_text(self, text):
        """Encrypt text using Base64"""
        try:
            encrypted = self.model_data.base64_encode(text)
            return {
                'success': True,
                'result': encrypted,
                'method': 'Base64 Encoding',
                'original': text
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def decrypt_text(self, text):
        """Decrypt text from Base64"""
        try:
            decrypted = self.model_data.base64_decode(text)
            return {
                'success': True,
                'result': decrypted,
                'method': 'Base64 Decoding',
                'original': text
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def check_password_strength(self, password):
        """Check password strength"""
        try:
            analysis = self.model_data.analyze_password_strength(password)
            return {
                'success': True,
                **analysis
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def ai_consultation(self, question):
        """Get AI consultation on security questions"""
        if not self.ai_available:
            return {
                'success': False,
                'error': 'AI service tidak tersedia'
            }
        
        try:
            prompt = f"""
            Sebagai Konsultan Keamanan Informasi profesional, jawab pertanyaan berikut:
            
            Pertanyaan: {question}
            
            PENTING: Jawab dalam format PLAIN TEXT, TANPA markdown formatting (*,**,#,|,```).
            Gunakan format:
            
            PENJELASAN:
            [Penjelasan singkat dan jelas dalam 2-3 paragraf]
            
            TIPS PRAKTIS:
            - [Tip 1]
            - [Tip 2]
            - [Tip 3]
            
            BEST PRACTICES:
            1. [Practice 1]
            2. [Practice 2]
            3. [Practice 3]
            
            Jawab dalam Bahasa Indonesia. Maksimal 400 kata.
            
            Jika pertanyaan terkait dengan:
            - Enkripsi: Jelaskan metode dan implementasinya
            - Password: Berikan tips keamanan password
            - Malware: Jelaskan jenis dan pencegahannya
            - Network Security: Jelaskan konsep dan toolsnya
            - Social Engineering: Jelaskan teknik dan cara menghindarinya
            """
            
            answer_text = self.call_gemini_api(prompt)
            
            return {
                'success': True,
                'answer': answer_text,
                'question': question
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def scan_vulnerability(self, input_text):
        """Scan for potential vulnerabilities"""
        if not self.ai_available:
            return {
                'success': False,
                'error': 'AI service tidak tersedia'
            }
        
        try:
            prompt = f"""
            Sebagai security auditor, analisis input berikut untuk kerentanan keamanan:
            
            Input: "{input_text}"
            
            PENTING: Jawab dalam PLAIN TEXT (tanpa markdown *, **, #, |, ```).
            
            JENIS INPUT: [URL/Code/Config/Text]
            
            VULNERABILITIES DITEMUKAN:
            - [Vulnerability 1]
            - [Vulnerability 2]
            
            SEVERITY: [Low/Medium/High/Critical]
            
            REKOMENDASI:
            1. [Rekomendasi 1]
            2. [Rekomendasi 2]
            3. [Rekomendasi 3]
            
            Bahasa Indonesia. Maksimal 250 kata.
            """
            
            analysis_text = self.call_gemini_api(prompt)
            
            # Simple pattern detection for common vulnerabilities
            vulnerabilities = []
            if 'SELECT' in input_text.upper() and ('OR' in input_text.upper() or '--' in input_text):
                vulnerabilities.append('Potensi SQL Injection')
            if '<script>' in input_text.lower():
                vulnerabilities.append('Potensi XSS (Cross-Site Scripting)')
            if '../' in input_text or '..\\' in input_text:
                vulnerabilities.append('Potensi Path Traversal')
            
            return {
                'success': True,
                'analysis': analysis_text,
                'quick_scan': vulnerabilities if vulnerabilities else ['Tidak ada vulnerability obvious terdeteksi'],
                'input': input_text
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def advanced_security_scan(self, scan_type, target):
        """Advanced AI Security Scanner with multiple scan types"""
        if not self.ai_available:
            return {
                'success': False,
                'error': 'AI service tidak tersedia'
            }
        
        try:
            # Different prompts based on scan type
            prompts = {
                'phishing': f"""
                Analisis URL/Email berikut untuk potensi phishing attack:
                
                Target: "{target}"
                
                PENTING: Format PLAIN TEXT (tanpa *, **, #, |, ```).
                
                HASIL ANALISIS:
                
                Status: [AMAN / MENCURIGAKAN / BERBAHAYA]
                
                Indikator Phishing Ditemukan:
                - [Indikator 1]
                - [Indikator 2]
                - [Indikator 3]
                
                Teknik Phishing:
                [Jelaskan teknik yang digunakan]
                
                Red Flags:
                - [Red flag 1]
                - [Red flag 2]
                
                Rekomendasi:
                1. [Langkah keamanan 1]
                2. [Langkah keamanan 2]
                3. [Langkah keamanan 3]
                
                Bahasa Indonesia. Maksimal 300 kata.
                """,
                
                'malware': f"""
                Analisis code/file signature berikut untuk potensi malware:
                
                Target: "{target}"
                
                PENTING: Format PLAIN TEXT (tanpa markdown).
                
                HASIL SCAN MALWARE:
                
                Threat Level: [LOW / MEDIUM / HIGH / CRITICAL]
                
                Potensi Malware Detected:
                - [Malware type 1]
                - [Malware type 2]
                
                Behavior Analysis:
                [Analisis perilaku suspicious]
                
                IoC (Indicators of Compromise):
                - [IoC 1]
                - [IoC 2]
                - [IoC 3]
                
                Mitigasi:
                1. [Langkah mitigasi 1]
                2. [Langkah mitigasi 2]
                3. [Langkah mitigasi 3]
                
                Quarantine Recommendation: [Ya/Tidak]
                
                Bahasa Indonesia. Maksimal 300 kata.
                """,
                
                'network': f"""
                Analisis konfigurasi network/firewall berikut:
                
                Config: "{target}"
                
                PENTING: Format PLAIN TEXT.
                
                NETWORK SECURITY AUDIT:
                
                Security Posture: [WEAK / MODERATE / STRONG]
                
                Vulnerabilities Found:
                - [Vulnerability 1]
                - [Vulnerability 2]
                - [Vulnerability 3]
                
                Open Ports & Services:
                [Analisis port dan service yang berisiko]
                
                Network Misconfigurations:
                - [Misconfig 1]
                - [Misconfig 2]
                
                Hardening Recommendations:
                1. [Hardening step 1]
                2. [Hardening step 2]
                3. [Hardening step 3]
                
                Compliance: [SOC2 / ISO27001 / PCI-DSS status]
                
                Bahasa Indonesia. Maksimal 300 kata.
                """,
                
                'social_engineering': f"""
                Analisis pesan/komunikasi berikut untuk social engineering attack:
                
                Pesan: "{target}"
                
                PENTING: Format PLAIN TEXT.
                
                SOCIAL ENGINEERING ANALYSIS:
                
                Attack Type: [Pretexting / Baiting / Quid Pro Quo / Tailgating / Lainnya]
                
                Manipulation Tactics:
                - [Taktik 1]
                - [Taktik 2]
                - [Taktik 3]
                
                Psychological Triggers:
                [Urgency / Fear / Authority / Curiosity / Greed yang digunakan]
                
                Warning Signs:
                - [Warning 1]
                - [Warning 2]
                - [Warning 3]
                
                Countermeasures:
                1. [Langkah pencegahan 1]
                2. [Langkah pencegahan 2]
                3. [Langkah pencegahan 3]
                
                Awareness Tips:
                [Tips untuk menghindari serangan]
                
                Bahasa Indonesia. Maksimal 300 kata.
                """,
                
                'data_leak': f"""
                Analisis data/credential berikut untuk potensi data leakage:
                
                Data: "{target}"
                
                PENTING: Format PLAIN TEXT.
                
                DATA LEAK ASSESSMENT:
                
                Risk Level: [LOW / MEDIUM / HIGH / CRITICAL]
                
                Sensitive Information Found:
                - [Info 1]
                - [Info 2]
                - [Info 3]
                
                Exposure Analysis:
                [Analisis tingkat eksposur data]
                
                Data Classification:
                [Public / Internal / Confidential / Restricted]
                
                Breach Indicators:
                - [Indikator 1]
                - [Indikator 2]
                
                Remediation Steps:
                1. [Langkah remediasi 1]
                2. [Langkah remediasi 2]
                3. [Langkah remediasi 3]
                
                DLP Recommendations:
                [Rekomendasi Data Loss Prevention]
                
                Bahasa Indonesia. Maksimal 300 kata.
                """
            }
            
            prompt = prompts.get(scan_type, prompts['phishing'])
            analysis_text = self.call_gemini_api(prompt)
            
            return {
                'success': True,
                'scan_type': scan_type,
                'analysis': analysis_text,
                'target': target,
                'timestamp': __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def analyze_hash(self, action, hash_value, password=''):
        """Analyze hash and optionally verify password"""
        try:
            import re
            import bcrypt
            
            # Detect hash type
            hash_info = {
                'hash': hash_value,
                'type': 'Unknown',
                'algorithm': 'Unknown',
                'length': len(hash_value),
                'can_decrypt': False,
                'security_level': 'Unknown'
            }
            
            # Bcrypt detection ($2a$, $2b$, $2y$)
            if re.match(r'^\$2[aby]\$\d{2}\$.{53}$', hash_value):
                hash_info['type'] = 'Bcrypt'
                hash_info['algorithm'] = 'Bcrypt (Blowfish)'
                hash_info['can_decrypt'] = False
                hash_info['security_level'] = 'Very Strong (One-way)'
                hash_info['cost_factor'] = hash_value.split('$')[2]
                hash_info['description'] = 'Bcrypt adalah password hashing function yang sangat aman. Hash ini TIDAK BISA di-decrypt karena menggunakan one-way cryptographic function.'
            
            # SHA256 detection (64 hex chars)
            elif re.match(r'^[a-fA-F0-9]{64}$', hash_value):
                hash_info['type'] = 'SHA-256'
                hash_info['algorithm'] = 'SHA-256 (Secure Hash Algorithm)'
                hash_info['can_decrypt'] = False
                hash_info['security_level'] = 'Strong (One-way)'
                hash_info['description'] = 'SHA-256 hash (64 karakter hex). Ini adalah one-way hash yang tidak bisa di-decrypt.'
            
            # MD5 detection (32 hex chars)
            elif re.match(r'^[a-fA-F0-9]{32}$', hash_value):
                hash_info['type'] = 'MD5'
                hash_info['algorithm'] = 'MD5 (Message Digest 5)'
                hash_info['can_decrypt'] = False
                hash_info['security_level'] = 'Weak (Deprecated)'
                hash_info['description'] = 'MD5 hash (32 karakter hex). TIDAK AMAN untuk password! Bisa di-crack dengan rainbow tables.'
            
            # SHA1 detection (40 hex chars)
            elif re.match(r'^[a-fA-F0-9]{40}$', hash_value):
                hash_info['type'] = 'SHA-1'
                hash_info['algorithm'] = 'SHA-1 (Secure Hash Algorithm 1)'
                hash_info['can_decrypt'] = False
                hash_info['security_level'] = 'Weak (Deprecated)'
                hash_info['description'] = 'SHA-1 hash (40 karakter hex). Sudah tidak aman, sebaiknya upgrade ke SHA-256 atau lebih.'
            
            # Base64 detection
            elif re.match(r'^[A-Za-z0-9+/]+=*$', hash_value):
                hash_info['type'] = 'Base64'
                hash_info['algorithm'] = 'Base64 Encoding'
                hash_info['can_decrypt'] = True
                hash_info['security_level'] = 'None (Not Encryption)'
                hash_info['description'] = 'Base64 adalah encoding, BUKAN enkripsi! Bisa di-decode dengan mudah.'
                
                # Try to decode
                try:
                    import base64
                    decoded = base64.b64decode(hash_value).decode('utf-8')
                    hash_info['decoded_value'] = decoded
                except:
                    hash_info['decoded_value'] = 'Error: Invalid Base64 or binary data'
            
            # Password verification for bcrypt
            if action == 'verify' and password and hash_info['type'] == 'Bcrypt':
                try:
                    is_match = bcrypt.checkpw(password.encode(), hash_value.encode())
                    hash_info['verification'] = {
                        'attempted': True,
                        'match': is_match,
                        'message': '✅ Password MATCH!' if is_match else '❌ Password TIDAK MATCH'
                    }
                except Exception as e:
                    hash_info['verification'] = {
                        'attempted': True,
                        'match': False,
                        'message': f'Error verifying: {str(e)}'
                    }
            
            return {
                'success': True,
                'hash_info': hash_info
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_security_dashboard_data(self):
        """Get data for security dashboard"""
        return {
            'tips': self.model_data.get_security_tips(),
            'stats': {
                'threats_detected': 0,
                'scans_performed': 0,
                'security_score': 85
            }
        }
