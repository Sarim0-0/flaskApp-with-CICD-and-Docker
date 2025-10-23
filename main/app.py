from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Flask Lab - Home</h1>", 200

@app.route('/health')
def health():
    return "OK", 200

@app.route('/data', methods=['POST'])
def data():
    payload = request.get_json(silent=True) or {}
    return jsonify({"received": payload}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
