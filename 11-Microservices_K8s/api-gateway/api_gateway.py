from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API Gateway is running!"})

@app.route('/backend')
def call_backend():
    response = requests.get("http://backend-service:5000/backend")
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
