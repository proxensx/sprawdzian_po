from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}
]

@app.get('/users')
def get_all_users():
    return jsonify({'users': users})

