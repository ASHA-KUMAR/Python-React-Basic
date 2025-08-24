from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notes = []

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json
    note = {"id": len(notes)+1, "text": data["text"]}
    notes.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(debug=True)
