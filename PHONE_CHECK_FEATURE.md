# 📱 Fitur Cek Nomor Telepon & Deteksi Spam

## Deskripsi
Fitur **Cek Nomor Telepon & Deteksi Spam** adalah alat keamanan informasi yang dirancang untuk membantu pengguna memverifikasi nomor telepon dan mengidentifikasi potensi ancaman seperti:
- 📞 Spam Telepon
- 🎣 Phishing
- 💰 Fraud/Penipuan
- 🎭 Social Engineering

## Cara Kerja

### Input
Pengguna dapat memasukkan nomor telepon dalam format:
- `0812xxxxxxx` (format Indonesia standar)
- `+6281xxxxxxx` (format internasional)
- `6281xxxxxxx` (format tanpa tanda +)

### Proses
1. **Validasi Format**: Sistem memvalidasi format nomor telepon
2. **Normalisasi**: Nomor diubah ke format standar internasional (+62)
3. **Analisis AI**: Google Gemini AI menganalisis nomor untuk:
   - Mengidentifikasi operator seluler
   - Mendeteksi ciri-ciri spam
   - Mengevaluasi tingkat risiko
   - Memberikan rekomendasi keamanan

### Output
Hasil analisis menampilkan:
- ✅ **Status Risiko**: AMAN / MEDIUM / TINGGI
- 📊 **Informasi Nomor**: Original, Ternormalisasi, Negara
- ⚠️ **Peringatan**: Indikasi spam, phishing, atau fraud
- 📝 **Analisis Detail**: Penjelasan komprehensif dari AI
- 💡 **Tips Keamanan**: Rekomendasi praktis

## Fitur & Keunggulan

### ✨ Fitur Utama
- **Validasi Format Otomatis**: Mengenali berbagai format nomor telepon Indonesia
- **Deteksi Risiko Cerdas**: Menggunakan AI untuk analisis mendalam
- **Interface User-Friendly**: Desain yang intuitif dan responsif
- **Tips Keamanan Terintegrasi**: Saran praktis untuk keselamatan pengguna
- **Verifikasi Status**: Menunjukkan status verifikasi nomor

### 🎯 Tingkat Risiko
- 🟢 **AMAN**: Nomor terlihat aman untuk dihubungi
- 🟡 **MEDIUM**: Ada indikasi potensi risiko, perlu hati-hati
- 🔴 **TINGGI**: Risiko tinggi, hindari memberikan data pribadi

## Lokasi Fitur

### UI Location
1. **Dashboard** → Quick Actions → Tombol "Cek Telepon"
2. **Navigation Bar** → "Cek Telepon"
3. **Direct URL** → `/phone-check`

## Implementasi Teknis

### Backend (Python/Flask)
```python
# Di: controllers/security_controller.py
def check_phone_number(self, phone_number):
    """Check phone number for spam and security threats"""
    # Validasi dan normalisasi nomor
    # Analisis dengan AI Gemini
    # Return hasil analisis dengan tingkat risiko
```

### Route (Flask Blueprint)
```python
# Di: routes.py
@main_bp.route('/phone-check', methods=['GET', 'POST'])
def phone_check():
    """Check phone number and detect spam"""
    # GET: Tampilkan halaman form
    # POST: Proses input dan return hasil
```

### Frontend (HTML/JavaScript)
```html
<!-- Di: templates/phone_check.html -->
<!-- Form input dengan validasi JavaScript -->
<!-- Display hasil analisis dengan styling yang baik -->
<!-- Tips keamanan terintegrasi di sidebar -->
```

## Contoh Penggunaan

### Input
- `0812 1234 5678`
- `+6281212345678`
- `6281212345678`

### Output Contoh
```
Status Risiko: MEDIUM
Nomor Original: 0812 1234 5678
Nomor Ternormalisasi: +6281212345678
Negara: Indonesia (+62)

Peringatan: 
⚠️ Indikasi potensi spam

Analisis Detail:
[AI analysis dari Gemini...]
```

## Tips Keamanan

### 5 Tips Utama
1. ✓ Jangan berikan data pribadi ke nomor tidak dikenal
2. ✓ Verifikasi identitas penelepon sebelum berbagi informasi
3. ✓ Waspada terhadap permintaan transfer uang mendesak
4. ✓ Gunakan fitur pemblokiran spam di ponsel Anda
5. ✓ Laporkan nomor mencurigakan ke operator telekomunikasi

## Integrasi Sistem

### Models
- `SecurityModel`: Untuk operasi keamanan dasar

### Controllers
- `SecurityController`: Handler logika dengan method `check_phone_number()`

### Views (Templates)
- `phone_check.html`: UI untuk fitur cek telepon

### Routes
- `/phone-check` (GET & POST): Route utama fitur

## Database (Opsional)
Fitur ini dapat diintegrasikan dengan:
- Database nomor telepon spam yang diketahui
- History cek nomor pengguna
- Log peringatan keamanan

## Pengembangan Masa Depan

### Fitur Tambahan yang Bisa Ditambahkan
- 📊 Analisis statistik spam per operator
- 🔔 Notifikasi real-time untuk nomor spam
- 💾 Simpan history cek nomor
- 📋 Database komunitas spam reports
- 🌐 API eksternal untuk verifikasi nomor
- 🤖 Machine learning untuk deteksi pattern

## Support & Troubleshooting

### Issue Umum
- **Format tidak valid**: Pastikan nomor minimal 8 digit dan maksimal 13 digit
- **AI tidak tersedia**: Cek koneksi internet dan API Key Gemini
- **Analisis lambat**: Tunggu proses AI selesai, bisa memakan waktu 3-5 detik

## Changelog
- **v1.0** (Initial Release)
  - ✓ Validasi format nomor telepon
  - ✓ Normalisasi ke format internasional
  - ✓ Analisis AI dengan Gemini
  - ✓ Deteksi risiko (AMAN/MEDIUM/TINGGI)
  - ✓ Interface user-friendly
  - ✓ Integrasi ke Dashboard dan Navbar

---

**Dikembangkan dengan ❤️ menggunakan Google Gemini AI**
