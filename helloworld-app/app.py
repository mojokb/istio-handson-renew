import os
import math
from flask import Flask, request
app = Flask(__name__)


@app.route('/hello')
def hello():
    version = os.environ.get('SERVICE_VERSION')

    # do some cpu intensive computation
    x = 0.0001
    for i in range(0, 1000000):
        x = x + math.sqrt(x)

    return f'Hello version: {version}, instance: {os.environ.get("HOSTNAME")}\n'


@app.route('/health')
def health():
    return 'Helloworld is healthy', 200


if __name__ == "__main__":
    app.run(host='::', threaded=True)
