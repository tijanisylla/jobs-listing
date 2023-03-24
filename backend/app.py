from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime
import uuid
from io import BytesIO
from base64 import b64encode
# DB
from connection import db, client
from users import create_user, get_users, update_user_by_id, delete_user_by_id, get_user_by_username
from jobs import create_job_post, get_job_post, update_job_post, delete_job_post, get_job_post_by_id, get_job_post_by_user_id, get_job_post_by_location, get_job_post_by_job_type, get_job_post_by_salary

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

# Format users


def format_user(users):
    return [{
        'id': user['id'],
        'username': user['username'],
        'email': user['email'],
        'password': user['password'],
        'profile_pic': user['profile_pic']
    } for user in users]
# Login with JWT and add it to the users table


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']

    queried_user = get_user_by_username(username)
    if queried_user:
        jwt_token = jwt.encode({'username': username, 'password': password, 'email': email,
                               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'user': queried_user, 'token': jwt_token}), 200
    else:
        return jsonify({'message': 'User does not exist'}), 400


# Register with JWT and check if the user already exists in the DB and add it to the users table if not
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    profile_pic = data['profile_pic']
    queried_user = get_user_by_username(username)
    if queried_user:
        return jsonify({'message': 'User already exists'}), 400
    else:
        created = create_user(username, email, password, profile_pic)
        formatted_user = format_user(created)
        jwt_token = jwt.encode({'username': username, 'password': password, 'email': email,
                               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'user': formatted_user, 'token': jwt_token}), 200


# Update user and save img to memory and add it to the users table with the new img
@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    profile_pic = data['profile_pic']
    # Save the image to memory
    img = BytesIO()
    profile_pic.save(img, 'JPEG')
    img.seek(0)
    print(img)
    # Encode the image to base64
    profile_pic = b64encode(img.read()).decode('utf-8')
    updated = update_user_by_id(
        user_id, username, password, email, profile_pic)
    return jsonify({'user': updated}), 200


# Delete user from the users table
@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = delete_user_by_id(user_id)
    return jsonify({'user': deleted}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
