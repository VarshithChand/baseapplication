from flask import Flask

app = Flask(__name__)   # ✅ MUST be named 'app'

@app.route('/')
def home():
    return "Hello from Flask + Gunicorn 🚀"