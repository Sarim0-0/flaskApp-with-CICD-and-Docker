from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask CI/CD Lab!"

@app.route('/health')
def health():
    return jsonify(status="OK"), 200

@app.route('/data', methods=['POST'])
def data():
    payload = request.get_json()
    return jsonify(message="Data received", data=payload), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
