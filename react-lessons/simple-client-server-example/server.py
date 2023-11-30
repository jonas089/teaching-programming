from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire application

@app.route('/react')
def react():
    response = jsonify("Hello from server! :D")
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True)