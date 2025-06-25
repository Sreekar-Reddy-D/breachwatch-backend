from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "BreachWatch API is running."

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    prefix = data['prefix']
    suffix = data['suffix']
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        return jsonify({'error': 'HIBP API failed'}), 500

    for line in res.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return jsonify({'pwned': True, 'count': count})
    return jsonify({'pwned': False, 'count': 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
