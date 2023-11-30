from flask import Flask
from flask import jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}
]


@app.get('/users')
def get_all_users():
    return jsonify(users), 200


@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


@app.post('/users')
def create_user():
    pass

@app.patch('/users/<id>')
def update_user(id):
    pass


@app.put('/users/<int:user_id>')
def replace_user(id):
    pass


@app.delete('/users/<int:user_id>')
def delete_user(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)