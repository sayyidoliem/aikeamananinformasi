# AI Keamanan Informasi

Platform keamanan informasi berbasis AI menggunakan Google Gemini untuk menganalisis ancaman, enkripsi data, dan konsultasi keamanan.

## 🚀 Fitur

- ✅ **Analisis Ancaman**: Deteksi dan analisis ancaman keamanan dengan AI
- ✅ **Enkripsi Data**: Enkripsi dan dekripsi data dengan Base64
- ✅ **Cek Password**: Analisis kekuatan password
- ✅ **Scan Vulnerability**: Identifikasi kerentanan keamanan (SQL Injection, XSS, dll)
- ✅ **Konsultasi AI**: Tanya jawab dengan AI tentang keamanan informasi

## 📋 Prasyarat

- Python 3.8 atau lebih tinggi
- API Key Google Gemini

## 🛠️ Instalasi

1. Clone repository atau download project
```bash
cd aikeamananinformasi
```

2. Buat virtual environment (opsional tapi direkomendasikan)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Konfigurasi file .env
File `.env` sudah dibuat dengan API key Anda. Pastikan file ini tidak di-commit ke repository public.

## 🚀 Menjalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di: `http://127.0.0.1:5000`

## 📁 Struktur Project

```
aikeamananinformasi/
├── app.py                      # Entry point aplikasi
├── config.py                   # Konfigurasi aplikasi
├── routes.py                   # Routing aplikasi
├── requirements.txt            # Dependencies
├── .env                        # Environment variables
├── .gitignore                  # Git ignore file
├── models/                     # Models (Data layer)
│   ├── __init__.py
│   └── security_model.py       # Model untuk keamanan
├── controllers/                # Controllers (Business logic)
│   ├── __init__.py
│   └── security_controller.py  # Controller keamanan + Gemini AI
└── templates/                  # Views (UI dengan Bootstrap)
    ├── base.html               # Base template
    ├── index.html              # Homepage
    ├── dashboard.html          # Dashboard
    ├── analyze.html            # Analisis ancaman
    ├── encrypt.html            # Enkripsi/dekripsi
    ├── vulnerability_scan.html # Scan vulnerability
    ├── ai_consultation.html    # Konsultasi AI
    ├── 404.html                # Error 404
    └── 500.html                # Error 500
```

## 🎨 Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **AI**: Google Gemini AI
- **Architecture**: MVC (Model-View-Controller)

## 🔐 Keamanan

- API Key disimpan di file `.env` (tidak di-commit ke repository)
- Password hashing menggunakan SHA256
- Input validation untuk mencegah injection attacks
- HTTPS direkomendasikan untuk production

## 📝 Catatan Pengembangan

### Models (`models/security_model.py`)
- Menangani logika data dan operasi keamanan dasar
- Hash password, enkripsi/dekripsi, analisis password strength

### Controllers (`controllers/security_controller.py`)
- Business logic dan integrasi dengan Gemini AI
- Menghubungkan models dengan views
- Handle request dan response

### Views (`templates/`)
- UI menggunakan Bootstrap 5
- Responsive design
- Interactive dengan JavaScript

### Routes (`routes.py`)
- Definisi endpoint API
- Route untuk setiap halaman

## 🌟 Cara Menggunakan

1. **Dashboard**: Lihat overview keamanan dan tips
2. **Analisis Ancaman**: Input teks/email mencurigakan untuk dianalisis
3. **Enkripsi**: Enkripsi atau dekripsi data Anda
4. **Scan Vulnerability**: Scan code atau URL untuk kerentanan
5. **Konsultasi AI**: Tanya apapun tentang keamanan informasi

## 📄 License

Project ini dibuat untuk keperluan pembelajaran.

## 👨‍💻 Developer

Dikembangkan dengan ❤️ menggunakan Flask dan Google Gemini AI

---

**⚠️ PENTING**: 
- Jangan share API key Anda ke public
- Gunakan HTTPS untuk production
- Update dependencies secara berkala untuk keamanan
