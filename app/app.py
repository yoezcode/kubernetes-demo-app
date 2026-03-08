from flask import Flask
import socket
import os


app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    version = os.getenv("APP_VERSION", "v1")
    return f"Hello from Pod: {hostname} - {version}\n"

@app.route("/health")
def health():
    return "OK\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)