from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import uuid

app = Flask(__name__)

client = MongoClient()
db = client.Colab8
users = db.users

output = []

@app.route('/users', methods=['GET'])
def get_users():
    for user in users.find():
        output.append({'name' : user['name'], 'email': user['email'], 'pwd': user['pwd']})

    return jsonify({'result' : output})

@app.route('/users/<name>', methods=['GET'])
def get_one_user(name):
    find_user = users.find_one({'name': name})

    if find_user:
        output = {'name' : find_user['name'], 'email': find_user['email'], 'pwd': find_user['pwd']}
    else:
        output = 'User is not found'
    
    return jsonify({'result' : output})

@app.route('/users', methods=['POST'])
def add_users():
    name = request.json['name']
    email = request.json['email']
    pwd = request.json['pwd']

    user_id = users.insert_one({'_id': uuid.uuid4().hex, 'name': name, 'email': email, 'pwd': pwd }).inserted_id
    look_user = users.find_one({'_id' : user_id})
    return jsonify(look_user)


if __name__ == '__main__':
    app.run(debug=True)
