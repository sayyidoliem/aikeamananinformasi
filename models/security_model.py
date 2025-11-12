import base64
import hashlib
from datetime import datetime

class SecurityModel:
    """Model untuk menangani data keamanan informasi"""
    
    def __init__(self):
        self.security_levels = {
            'low': 'Rendah',
            'medium': 'Sedang',
            'high': 'Tinggi',
            'critical': 'Kritis'
        }
        
    def hash_password(self, password):
        """Hash password menggunakan SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def simple_encrypt(self, text, shift=3):
        """Simple Caesar cipher encryption"""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    def simple_decrypt(self, text, shift=3):
        """Simple Caesar cipher decryption"""
        return self.simple_encrypt(text, -shift)
    
    def base64_encode(self, text):
        """Encode text to base64"""
        return base64.b64encode(text.encode()).decode()
    
    def base64_decode(self, text):
        """Decode base64 to text"""
        try:
            return base64.b64decode(text.encode()).decode()
        except:
            return "Error: Invalid base64 string"
    
    def analyze_password_strength(self, password):
        """Analyze password strength"""
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password terlalu pendek (minimal 8 karakter)")
        
        if len(password) >= 12:
            score += 1
            
        # Check for uppercase
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan huruf besar")
            
        # Check for lowercase
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan huruf kecil")
            
        # Check for digits
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan angka")
            
        # Check for special characters
        if any(not c.isalnum() for c in password):
            score += 1
        else:
            feedback.append("Tambahkan karakter khusus (!@#$%^&*)")
        
        # Determine strength
        if score >= 5:
            strength = "Kuat"
            level = "high"
        elif score >= 3:
            strength = "Sedang"
            level = "medium"
        else:
            strength = "Lemah"
            level = "low"
            
        return {
            'strength': strength,
            'level': level,
            'score': score,
            'max_score': 6,
            'feedback': feedback
        }
    
    def get_security_tips(self):
        """Get security tips"""
        return [
            {
                'title': 'Gunakan Password yang Kuat',
                'description': 'Kombinasikan huruf besar, kecil, angka, dan simbol',
                'icon': 'lock'
            },
            {
                'title': 'Aktifkan Two-Factor Authentication',
                'description': 'Tambahkan lapisan keamanan ekstra pada akun Anda',
                'icon': 'shield-check'
            },
            {
                'title': 'Update Software Secara Berkala',
                'description': 'Pastikan sistem dan aplikasi selalu ter-update',
                'icon': 'arrow-repeat'
            },
            {
                'title': 'Waspada Terhadap Phishing',
                'description': 'Jangan klik link mencurigakan atau berikan data pribadi',
                'icon': 'exclamation-triangle'
            },
            {
                'title': 'Backup Data Secara Rutin',
                'description': 'Lindungi data penting dengan backup berkala',
                'icon': 'cloud-upload'
            },
            {
                'title': 'Gunakan VPN di Jaringan Publik',
                'description': 'Enkripsi koneksi internet saat menggunakan WiFi publik',
                'icon': 'wifi'
            }
        ]
