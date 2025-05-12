from flask import Flask, request, jsonify
import jwt
import datetime
import os

app = Flask(__name__)

# Constantes de seguridad
API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "123456"  

@app.route('/DevOps', methods=['POST'])
def devops():
    # Validar API Key
    if request.headers.get('X-Parse-REST-API-Key') != API_KEY:
        return jsonify({"error": "API Key inválida"}), 401

    # Obtener datos del cuerpo JSON
    try:
        data = request.get_json()
        to = data["to"]
    except Exception:
        return jsonify({"error": "Formato JSON inválido"}), 400

    # Generar JWT único
    jwt_payload = {
        "to": to,
        "iat": datetime.datetime.utcnow()
    }
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET, algorithm="HS256")

    # Respuesta
    hostname = os.getenv("HOSTNAME", "default")
    response = {
        "message": f"Hello {to} your message will be sent from {hostname}"
    }
    return jsonify(response), 200

# Rechazar otros métodos (GET, PUT, etc.)
@app.errorhandler(405)
def method_not_allowed(error):
    return "ERROR", 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


