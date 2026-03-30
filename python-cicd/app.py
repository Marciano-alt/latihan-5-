from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Python + Vercel berhasil 🚀"

@app.route("/about")
def about():
    return "Ini project deployment otomatis pakai Vercel"

app = app