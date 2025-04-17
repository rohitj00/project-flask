from flask import Flask, jsonify, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    res = {
        'timestamp': curr_time,
        'ip': ip
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
