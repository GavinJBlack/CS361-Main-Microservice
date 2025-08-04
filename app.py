# app.py

from flask import Flask, request, jsonify
from classifier import classify_command

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if not data or 'command' not in data:
        return jsonify({'error': 'Missing "command" in request'}), 400

    command = data['command']
    command_type = classify_command(command)
    return jsonify({'type': command_type}), 200

if __name__ == '__main__':
    app.run(debug=True)
