from flask import Blueprint, render_template, request, jsonify
from controllers.security_controller import SecurityController

# Create Blueprint
main_bp = Blueprint('main', __name__)
security_controller = SecurityController()

@main_bp.route('/')
def index():
    """Home page - Dashboard"""
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    """Dashboard page"""
    return render_template('dashboard.html')

@main_bp.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """Analyze security threats"""
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '')
        result = security_controller.analyze_security_threat(text)
        return jsonify(result)
    return render_template('analyze.html')

@main_bp.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    """Encrypt and decrypt data"""
    if request.method == 'POST':
        data = request.get_json()
        action = data.get('action', 'encrypt')
        text = data.get('text', '')
        
        if action == 'encrypt':
            result = security_controller.encrypt_text(text)
        else:
            result = security_controller.decrypt_text(text)
        
        return jsonify(result)
    return render_template('encrypt.html')

@main_bp.route('/check-password', methods=['POST'])
def check_password():
    """Check password strength"""
    data = request.get_json()
    password = data.get('password', '')
    result = security_controller.check_password_strength(password)
    return jsonify(result)

@main_bp.route('/ai-consultation', methods=['GET', 'POST'])
def ai_consultation():
    """AI consultation for security questions"""
    if request.method == 'POST':
        data = request.get_json()
        question = data.get('question', '')
        result = security_controller.ai_consultation(question)
        return jsonify(result)
    return render_template('ai_consultation.html')

@main_bp.route('/vulnerability-scan', methods=['GET', 'POST'])
def vulnerability_scan():
    """Scan for vulnerabilities"""
    if request.method == 'POST':
        data = request.get_json()
        url_or_text = data.get('input', '')
        result = security_controller.scan_vulnerability(url_or_text)
        return jsonify(result)
    return render_template('vulnerability_scan.html')

@main_bp.route('/advanced-scanner', methods=['GET', 'POST'])
def advanced_scanner():
    """Advanced AI Security Scanner"""
    if request.method == 'POST':
        data = request.get_json()
        scan_type = data.get('scan_type', '')
        target = data.get('target', '')
        result = security_controller.advanced_security_scan(scan_type, target)
        return jsonify(result)
    return render_template('advanced_scanner.html')

@main_bp.route('/hash-analyzer', methods=['GET', 'POST'])
def hash_analyzer():
    """Hash Analyzer and Verifier"""
    if request.method == 'POST':
        data = request.get_json()
        action = data.get('action', 'analyze')
        hash_value = data.get('hash', '')
        password = data.get('password', '')
        result = security_controller.analyze_hash(action, hash_value, password)
        return jsonify(result)
    return render_template('hash_analyzer.html')
