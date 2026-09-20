import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enforce secure CORS policy matching your GitHub Pages live instance
CORS(app, resources={r"/api/*": {"origins": ["https://github.io", "http://localhost:3000"]}})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "Sojan-Portfolio-Core"}), 200

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid payload body"}), 400
            
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({"error": "Missing mandatory fields"}), 422
            
        # Log payload processing to stdout for cloud environment aggregation
        print(f"[SYSTEM LOG] Ingested message from {name} <{email}>: {message}")
        
        return jsonify({
            "status": "success",
            "message": f"Handshake verified. Thank you, {name}. Data piped successfully."
        }), 200

    except Exception as e:
        print(f"[CRITICAL ERROR] Execution failed: {str(e)}")
        return jsonify({"error": "Internal Server Error Processing Request Node"}, str(e)), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
