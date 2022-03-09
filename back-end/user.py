from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from database import *
import uuid

user = Blueprint("user", __name__)

# Users
@user.route('/', methods=['GET'])
def get_users():
    output = []
    for user in users.find():
        output.append({'name' : user['name'], 'phone_number': user['phone_number'], 'password': user['password']})

    return jsonify({'result' : output})

@user.route('/<phone_number>', methods=['GET'])
def get_one_user(name):
    find_user = users.find_one({'name': name})

    if find_user:
        output = {'name' : find_user['name'], 'phone_number': find_user['phone_number'], 'password': find_user['password']}
    else:
        output = 'User is not found'
    
    return jsonify({'result' : output})

@user.route('/', methods=['POST'])
def add_users():
    name = request.json['name']
    phone_number = request.json['phone_number']
    password = request.json['password']

    user_id = users.insert_one({'_id': uuid.uuid4().hex, 'name': name, 'phone_number': phone_number, 'password': password }).inserted_id
    look_user = users.find_one({'_id' : user_id})
    return jsonify(look_user)
