from flask import Blueprint, request, jsonify, session, abort
from bson.objectid import ObjectId
from database import *
import uuid
import bcrypt

user = Blueprint("user", __name__)

@user.errorhandler(403)
def forbidden(e):
    return jsonify(error=str(e)), 403

@user.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

# @user.errorhandler(404)
# def not_found(e):
#     return jsonify(error=str(e)), 404

# User
@user.route('/signup', methods=['POST']) # Sign up Page
def signup():
    if 'current_user' in session:
        abort(403, description='You already signed in')

    name = request.json['name']
    phone_number = request.json['phone_number']
    password = request.json['password']

    if users.find_one({'phone_number': phone_number}):
        abort(403, description='The phone number already exists!')
    if validate_number(phone_number): # +1 123-456-7890
        if len(password) < 8:
            abort(403, description='Password needs to be minimum 8 characters')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_id = users.insert_one({
            '_id': uuid.uuid4().hex,
            'name': name,
            'phone_number': phone_number,
            'password': hashed_password
        }).inserted_id

        new_user = users.find_one({'_id': user_id})
        session['current_user'] = new_user
        return jsonify([{'name' : new_user['name'], 'phone_number': new_user['phone_number']}]), 201
    else:
        abort(403, description='Type the correct number')

@user.route('/signin', methods=['POST'])
def signin():
    if 'current_user' in session:
        return jsonify({'Error' : 'You already signed in'}), 203
# Maybe status 404
    phone_number = request.json['phone_number']
    user = users.find_one({'phone_number' : phone_number})
    if user:
        if bcrypt.hashpw(request.json['password'].encode('utf-8'), user['password']) == user['password']:
            session['current_user'] = user
            return jsonify([{'name' : user['name'], 'phone_number': user['phone_number']}]), 200
    
    abort(400, description='Invalid email/password combination')

@user.route('/logout', methods=['POST'])
def logout():
    if 'current_user' in session:
        session.pop('current_user', None)
    return jsonify({'message' : 'You successfully logged out'}), 200

@user.route('/', methods=['GET'])
def index():
    all_users = []
    for user in users.find():
        all_users.append({'_id': user['_id'], 'name' : user['name'], 'phone_number': user['phone_number']})
    return jsonify({'result' : all_users}), 200

@user.route('/<user_id>', methods=['GET'])
def get_one_user(user_id):
    user = users.find_one({'_id': user_id})
    if user:
        del user['password']
        return jsonify({'result': user}), 200

    abort(404, description='User is not found')

