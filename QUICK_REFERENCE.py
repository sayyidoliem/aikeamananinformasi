#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUICK REFERENCE - Fitur Cek Nomor Telepon & Spam Detection
Version: 1.0.0
Date: November 16, 2025
"""

"""
╔════════════════════════════════════════════════════════════════════════════╗
║           📱 CEK NOMOR TELEPON & DETEKSI SPAM - QUICK REFERENCE            ║
╚════════════════════════════════════════════════════════════════════════════╝

🎯 AKSES FITUR
═══════════════════════════════════════════════════════════════════════════════

1️⃣  Dari Dashboard
    → Dashboard → Quick Actions → "Cek Telepon"
    URL: http://127.0.0.1:5000/dashboard

2️⃣  Dari Navigation Bar
    → Klik "Cek Telepon" di menu atas
    URL: http://127.0.0.1:5000/phone-check

3️⃣  Direct URL
    → http://127.0.0.1:5000/phone-check

📋 FORMAT INPUT NOMOR
═══════════════════════════════════════════════════════════════════════════════

Fitur mendukung berbagai format nomor telepon Indonesia:

✅ Format yang didukung:
   • 0812345678        (9-13 digit, dimulai dengan 0)
   • +6281234567       (Format internasional dengan +)
   • 6281234567        (Format internasional tanpa +)
   • 0812 345 678      (Dengan spasi)
   • 0812-345-678      (Dengan dash)
   • 0812.345.678      (Dengan titik)
   • (081) 234-5678    (Dengan parenthesis & dash)

❌ Format yang tidak didukung:
   • 081                (Terlalu pendek, < 8 digit)
   • 08123456789012345 (Terlalu panjang, > 13 digit)
   • +62 812 3456789   (Format yang tidak konsisten)

🔍 CARA MENGGUNAKAN
═══════════════════════════════════════════════════════════════════════════════

Langkah 1: Masukkan Nomor
  → Input nomor telepon di field yang tersedia
  → Bisa copy-paste dari sumber lain

Langkah 2: Klik "Cek Nomor Telepon"
  → Tombol besar berwarna biru di tengah
  → Atau tekan Enter di keyboard

Langkah 3: Tunggu Proses
  → Loading spinner akan muncul (3-5 detik)
  → AI Gemini sedang menganalisis nomor

Langkah 4: Analisis Hasil
  → Baca Status Risiko (AMAN/MEDIUM/TINGGI)
  → Lihat informasi nomor yang dinormalisasi
  → Periksa warning jika ada
  → Baca analisis detail dari AI
  → Terapkan tips keamanan

📊 TINGKAT RISIKO
═══════════════════════════════════════════════════════════════════════════════

🟢 AMAN
   ✓ Nomor terlihat aman untuk dihubungi
   ✓ Tidak ada indikasi spam atau phishing
   ✓ Rekomendasi: Aman menerima panggilan

🟡 MEDIUM
   ⚠ Ada beberapa indikasi risiko
   ⚠ Perlu hati-hati dalam berbagi info
   ⚠ Rekomendasi: Verifikasi identitas dulu

🔴 TINGGI
   🚨 Risiko tinggi terdeteksi
   🚨 Hindari memberikan informasi pribadi
   🚨 Rekomendasi: Pertimbangkan memblokir nomor

⚠️ INDIKASI RISIKO YANG MUNGKIN TERDETEKSI
═══════════════════════════════════════════════════════════════════════════════

📞 SPAM TELEPON
   • Panggilan masif tanpa konteks
   • Penawaran produk tidak jelas
   • Permintaan klik link mencurigakan

🎣 PHISHING
   • Meminta verifikasi data pribadi
   • Menyamar sebagai institusi terpercaya
   • Urgent tone untuk memaksa action

💰 FRAUD/PENIPUAN
   • Permintaan transfer uang mendesak
   • Cerita fiktif untuk meminta uang
   • Jackpot atau hadiah palsu

🎭 SOCIAL ENGINEERING
   • Membangun kepercayaan palsu
   • Memanipulasi emosi (takut, excitement)
   • Meminta informasi sensitif secara halus

💡 TIPS KEAMANAN
═══════════════════════════════════════════════════════════════════════════════

1️⃣  JANGAN berikan data pribadi
    ❌ No: Nomor KTP, Tanggal lahir, PIN, Password
    ✅ Yes: Nama umum, Tanya identitas balik

2️⃣  VERIFIKASI identitas penelepon
    ✓ Tanya nama lengkap & institusi
    ✓ Tanya nomor reference/kasus
    ✓ Call back ke nomor resmi dari web

3️⃣  WASPADA permintaan mendesak
    ⚠ Red flags: "Segera!", "Terbatas!", "Terakhir!"
    ⚠ Berikan waktu untuk investigasi sendiri

4️⃣  GUNAKAN pemblokiran spam
    📱 Di Android: Settings → Apps & notifications → Call Filter
    📱 Di iPhone: Settings → Phone → Silence Unknown Callers
    📱 Gunakan aplikasi: Truecaller, ACR, Call Blocker

5️⃣  LAPORKAN nomor mencurigakan
    📋 Ke operator: Buka app operator → Report spam
    📋 Ke Kominfo: Lapor.go.id
    📋 Ke database komunitas: Truecaller, Whoscall

🛠️ IMPLEMENTASI TEKNIS
═══════════════════════════════════════════════════════════════════════════════

Backend (Python/Flask)
  → File: controllers/security_controller.py
  → Method: check_phone_number(phone_number)
  → Logic: Validasi → Normalisasi → AI Analysis

API Endpoint
  → URL: /phone-check
  → Method: POST
  → Content-Type: application/json
  → Request: {"phone": "0812345678"}
  → Response: {...result...}

Frontend (HTML/JavaScript)
  → File: templates/phone_check.html
  → Validasi input di client side
  → AJAX request ke backend
  → Display hasil dengan styling

Database Integration
  → Optional: Simpan history cek
  → Optional: Spam database komunitas
  → Optional: User preferences

📱 TAMPILAN UI
═══════════════════════════════════════════════════════════════════════════════

Header Section
├─ Title: "🔒 Cek Nomor Telepon & Deteksi Spam"
├─ Subtitle: "Verifikasi nomor dan identifikasi potensi spam, phishing, fraud"
└─ Icon: <i class="bi bi-telephone-fill"></i>

Input Section
├─ Input Field dengan icon telepon
├─ Placeholder: "Contoh: 0812xxxx, +628xx, atau 628xx"
├─ Help text: Format yang didukung
└─ CTA Button: "Cek Nomor Telepon" (Primary)

Result Section (setelah submit)
├─ Risk Badge dengan warna sesuai level
├─ Warning Box (jika ada indikasi risiko)
├─ Phone Info Grid (4 items)
│  ├─ Nomor Original
│  ├─ Nomor Ternormalisasi
│  ├─ Negara
│  └─ Status Verifikasi
├─ Analysis Section
│  └─ Hasil detail dari AI
└─ Loading Spinner (saat proses)

Sidebar Tips
├─ Cara Penggunaan (numbered list)
├─ Tips Keamanan (5 tips utama)
└─ Informasi (apa yang dideteksi)

🔧 TROUBLESHOOTING
═══════════════════════════════════════════════════════════════════════════════

Problem: "Format nomor telepon tidak valid"
Solution:
  → Pastikan nomor minimal 8 digit
  → Pastikan nomor maksimal 13 digit
  → Gunakan salah satu format yang didukung
  → Contoh: 0812345678 (BENAR), 081 (SALAH)

Problem: "AI tidak tersedia"
Solution:
  → Cek koneksi internet
  → Cek API Key Gemini di config.py
  → Lihat server logs untuk error detail
  → Restart server: python app.py

Problem: "Halaman tidak muncul"
Solution:
  → Clear browser cache (Ctrl+F5)
  → Check URL: http://127.0.0.1:5000/phone-check
  → Buka browser DevTools (F12) → Console
  → Lihat error message yang muncul

Problem: "Form submit tidak bekerja"
Solution:
  → Cek browser console (F12)
  → Lihat Network tab untuk request
  → Pastikan server masih berjalan
  → Coba refresh halaman

Problem: "Analisis memakan waktu lama"
Solution:
  → Normal: 3-5 detik (AI processing)
  → Jika > 10 detik: Cek koneksi internet
  → Jika stuck: Refresh halaman, submit lagi

📊 API REFERENCE
═══════════════════════════════════════════════════════════════════════════════

Endpoint: POST /phone-check

Request Example:
{
    "phone": "0812345678"
}

Response Success (200):
{
    "success": true,
    "number": {
        "original": "0812 345 678",
        "normalized": "+6281234567",
        "cleaned": "081234567",
        "country": "Indonesia (+62)",
        "analysis": "[AI analysis text]",
        "risk_level": "MEDIUM"
    },
    "warnings": [
        "⚠️ Indikasi potensi spam"
    ],
    "verified": true
}

Response Error (400):
{
    "success": false,
    "error": "Format nomor telepon tidak valid. Gunakan format: 0812xxxx, +6281xxxx, atau 62812xxxx"
}

Response Error (500):
{
    "success": false,
    "error": "Error message dari server"
}

🚀 DEPLOYMENT
═══════════════════════════════════════════════════════════════════════════════

Untuk production:
1. Set FLASK_ENV = production
2. Gunakan production WSGI (Gunicorn, uWSGI)
3. Enable HTTPS/SSL
4. Setup rate limiting untuk API
5. Add database untuk history
6. Setup logging & monitoring
7. Backup & disaster recovery

📝 DOKUMENTASI
═══════════════════════════════════════════════════════════════════════════════

File dokumentasi yang tersedia:
  • PHONE_CHECK_FEATURE.md - Dokumentasi lengkap fitur
  • IMPLEMENTATION_SUMMARY.md - Ringkasan implementasi
  • QUICK_REFERENCE.txt - File ini

📚 LEARNING RESOURCES
═══════════════════════════════════════════════════════════════════════════════

• Flask Documentation: https://flask.palletsprojects.com
• Google Gemini API: https://ai.google.dev
• Bootstrap 5: https://getbootstrap.com/docs/5.0
• Regex Patterns: https://regex101.com

🎓 VERSION HISTORY
═══════════════════════════════════════════════════════════════════════════════

v1.0.0 (November 16, 2025) - Initial Release
  ✓ Phone number validation
  ✓ Format normalization
  ✓ AI-powered analysis
  ✓ Risk level detection
  ✓ Dashboard integration
  ✓ Navbar integration
  ✓ Full documentation

🏆 FEATURE HIGHLIGHTS
═══════════════════════════════════════════════════════════════════════════════

✨ Smart Validation      → Recognizes various formats
✨ AI-Powered Analysis   → Uses Google Gemini
✨ Risk Detection        → AMAN/MEDIUM/TINGGI levels
✨ User-Friendly         → Intuitive interface
✨ Responsive Design     → Works on all devices
✨ Security Tips         → Practical advice
✨ Beautiful UI          → Modern styling
✨ Integrated            → Dashboard & Navbar ready

✅ STATUS: PRODUCTION READY

═══════════════════════════════════════════════════════════════════════════════

Generated: November 16, 2025
Author: AI Assistant
Version: 1.0.0

═══════════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(__doc__)
