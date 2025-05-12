from flask import Flask, request, jsonify
import datetime
import jwt
import os

app = Flask(__name__)


@app.route('/DevOps', methods=['POST'])
def devops():
    api_key = request.headers.get("X-Parse-REST-API-Key")
    if api_key != "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c":
        return jsonify({"message": "Unauthorized"}), 401

    data = request.get_json()
    message = data.get("message")
    to = data.get("to")
    from_ = data.get("from")
    time_to_live_sec = data.get("timeToLifeSec")

    jwt_payload = {
        "to": to,
        "from": from_,
        "message": message,
        "timeToLifeSec": time_to_live_sec,
        "iat": datetime.datetime.utcnow()
    }

    secret_key = "secret"
    jwt_token = jwt.encode(jwt_payload, secret_key, algorithm="HS256")

    hostname = os.getenv("HOSTNAME", "local")
    response = {
        "message": f"Hello {to} your message will be sent from {hostname}",
        "token": jwt_token
    }

    return jsonify(response), 200  # Success


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    