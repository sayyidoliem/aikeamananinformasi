from flask import Flask, render_template
from config import Config
from routes import main_bp
import os

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    Config.init_app(app)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     🛡️  AI KEAMANAN INFORMASI SYSTEM 🛡️                  ║
    ║                                                           ║
    ║     Powered by Google Gemini AI                          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    🚀 Aplikasi berjalan di: http://127.0.0.1:5000
    
    📋 Fitur yang tersedia:
       ✓ Analisis Ancaman Keamanan dengan AI
       ✓ Enkripsi & Dekripsi Data
       ✓ Cek Kekuatan Password
       ✓ Scan Vulnerability
       ✓ Konsultasi AI 24/7
       ✓ Cek Nomor Telepon & Deteksi Spam (NEW!)
    
    💡 Tekan CTRL+C untuk menghentikan server
    """)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
