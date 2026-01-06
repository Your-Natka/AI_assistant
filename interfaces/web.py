from flask import Flask, request, jsonify
from core.ai import ask_ai

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    text = request.json["text"]
    return jsonify({"answer": ask_ai(text)})

app.run()
