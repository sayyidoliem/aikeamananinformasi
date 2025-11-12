@echo off
echo ========================================
echo   AI Keamanan Informasi - Setup
echo ========================================
echo.

echo [1/3] Membuat Virtual Environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Gagal membuat virtual environment
    pause
    exit /b 1
)

echo [2/3] Mengaktifkan Virtual Environment...
call venv\Scripts\activate.bat

echo [3/3] Menginstall Dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Gagal menginstall dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Selesai!
echo ========================================
echo.
echo Untuk menjalankan aplikasi:
echo 1. Aktifkan virtual environment: venv\Scripts\activate
echo 2. Jalankan aplikasi: python app.py
echo.
pause
