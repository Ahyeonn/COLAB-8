from flask import Blueprint, request, jsonify, session, abort
from bson.objectid import ObjectId
from extensions import *
import uuid
import bcrypt
from utils import validate_number


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

@user.route('/events', methods=['GET'])
def dashboard_index():
    user = users.find_one({'phone_number': request.json['phoneNumber']})
    user_events = [e for e in events.find({'owner_id': user['_id']})]

    if user_events:
        display_events = []
        for event in user_events:
            event_detail = {
                'num_of_recipients': len(event['recipients']),
                'event_name' : (event['event_name']),
                'event_id' : (event['_id'])
            }
            display_events.append(event_detail)

        return jsonify([{ 'events' : user_events }]), 200
    else:
        return jsonify({'message' : 'No events'})

# @user.route('dashboard/<event_id>', methods=['GET'])
# def dashboard_detail(event_id):
#     event = events.find_one({'_id': event_id})
#     event_rsvps = rsvps.find({'event_id': event_id})

#     return render_template('events_show.html', event=event, rsvps=event_rsvps)

#     if 'current_user' in session:
#         user = users.find_one({'phone_number': session['current_user']['phone_number']})
#         user_events = [e for e in events.find({'owner_id': user['_id']})]
#         # event_detail = [e for e in events.find_one({'event_id': user_events['_id']})]
#         print(event_detail)

#         # event_detail = user_events.find_one({'_id': event_id})
#         # print(event_detail)

#         if user_events:
#             return jsonify([{ 'event_name' : user_events[0]['event_name'], 'host_name' : user_events[0]['name'], 'date' : user_events[0]['date'], 'time' : user_events[0]['time'], 'recipients' : user_events[0]['recipients'] }]), 200
#         else:
#             return jsonify({'message' : 'No events'})
    
#     return jsonify({'message' : 'Please sign in'})

# User
@user.route('/signup', methods=['GET', 'POST']) # Sign up Page
def signup():
    if request.method == 'GET': return jsonify({'message' : 'Please sign up'})

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
        return jsonify([{'name' : new_user['name'], 'phone_number': new_user['phone_number']}]), 201
    else:
        abort(403, description='Type the correct number')

@user.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'GET': return jsonify({'message' : 'Please sign in'})
# Maybe status 404
    phone_number = request.json['phone_number']
    user = users.find_one({'phone_number': phone_number})
    if user:
        if bcrypt.hashpw(request.json['password'].encode('utf-8'), user['password']) == user['password']:
            return jsonify([{'name' : user['name'], 'phone_number': user['phone_number']}]), 200
    
    abort(400, description='Invalid email/password combination')

@user.route('/logout', methods=['POST', 'GET'])
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

#If signed in
@user.route('/<user_id>', methods=['GET'])
def show_user(user_id):
    user = users.find_one({'_id': user_id})
    if user:
        user_events = [e for e in events.find({'owner_id': user_id})]
        return jsonify({'result': user_events}), 200

    abort(404, description='User is not found')

