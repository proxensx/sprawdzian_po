from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

app = Flask(__name__)

users = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}
]


@app.get('/users')
def get_all_users():
    return jsonify(users), 200


def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None


@app.get('/users/<int:user_id>')
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


@app.post('/users')
def create_user():
    data = request.get_json()
    if 'name' in data and 'lastname' in data:
        user = {
            'id': len(users) + 1,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(user)
        return '', 201
    return jsonify({'error': 'Invalid request body'}), 400


@app.patch('/users/<id>')
def update_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        data = request.get_json()
        if 'name' in data:
            user['name'] = data['name']
        if 'lastname' in data:
            user['lastname'] = data['lastname']
        return '', 204
    return jsonify({'error': 'User not found'}), 404


@app.put('/users/<int:user_id>')
def replace_user(user_id):
    user = get_user_by_id(user_id)
    data = request.get_json()
    if user:
        user['name'] = data['name']
        user['lastname'] = data['lastname']
        return '', 204
    else:
        new_user = {
            'id': user_id,
            'name': data['name'],
            'lastname': data['lastname']
        }
        users.append(new_user)
        return '', 201


@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        users.remove(user)
        return jsonify(), 204
    else:
        return jsonify({'error': 'User not found'}), 404



@app.route('/')
def index():
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run()