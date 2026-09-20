from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# This allows your GitHub Pages site to talk to this API
CORS(app)

# 1. Health Check Endpoint (Render uses this to monitor your app)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "API is running smoothly"}), 200

# 2. Contact Form Endpoint
@app.route('/contact', methods=['POST'])
def contact_form():
    # Safely get JSON data sent from your index.html
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    # Validation check
    if not name or not email or not message:
        return jsonify({"error": "Missing required fields"}), 400
        
    # TODO: Process your message here (e.g., send an email, save to database, etc.)
    print(f"New message from {name} ({email}): {message}")
    
    return jsonify({
        "success": True,
        "message": f"Thank you, {name}! Your message has been received."
    }), 200

if __name__ == '__main__':
    # Flask runs locally on port 5000; Render will use Gunicorn in production
    app.run(host='0.0.0.0', port=5000)
