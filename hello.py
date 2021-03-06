from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from host \"%s\".\n' % socket.gethostname()

@app.route('/sri')
def hellosri():
    return 'Hello Sri from  \"%s\".\n' % socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
