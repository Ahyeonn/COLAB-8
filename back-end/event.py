from flask import Blueprint, request, jsonify, abort, session
from bson.objectid import ObjectId
# from twilio_api import create_rsvp
from extensions import *
import uuid
from utils import validate_number

event = Blueprint("event", __name__)

@event.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

@event.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

# Events
@event.route('/', methods=['GET'])
def index():
    output = [event for event in events.find()]

    return jsonify({'events' : output}), 200

@event.route('/create', methods=['POST'])
def create_event():
    event_id = request.json['event_id']
    owner_id = session['current_user']['_id'] if 'current_user' in session else None
    owner_name = request.json['name']
    event_name = request.json['event_name']
    # host_phone = request.json['host_phone']
    # recipients = request.json['recipients']
    # recipients = []
    date = request.json['date']
    time = request.json['time']
    # contacts = {}

    # for name, phone_number in recipients.items():
        # if validate_number(phone_number):
        #     contacts[name] = phone_number

#     event_id = events.insert_one({'_id': uuid.uuid4().hex, 'owner_id': owner_id, 'name': owner_name, 'event_name': event_name, 'date': date, 'recipients': contacts, 'time': time}).inserted_id

    event_id = events.insert_one({'_id': event_id, 'owner_id': owner_id, 'name': owner_name, 'event_name': event_name, 'date': date, 'time': time}).inserted_id
    new_event = events.find_one({'_id' : event_id})
    return jsonify(new_event), 200


#If Signed in 
@event.route('/user/<user_id>', methods=['GET'])
def get_events_by_user(user_id):
    output = [e for e in events.find({'owner_id': user_id})]
    if output:
        return jsonify({'events result' : output}), 200

    abort(404, description='not found')

@event.route('/<event_id>', methods=['GET'])
def show_event(event_id):
    event = events.find_one({'_id': event_id})
    if event:
        return jsonify({'event result' : event}), 200

    abort(404, description='not found')

@event.route('/add_user', methods=['POST'])
def add_user_event():
    recipients = request.json['meetingMembers']['contacts']
    event_id = request.json['meetingMembers']['eventId']
    for recipient in recipients:
        new_recipient = {
            'name': recipient['name'],
            'phone_number': recipient['phoneNumber']
        }
        if validate_number(new_recipient['phone_number']):
            events.update_one({'_id': event_id}, {'$push':{'recipients': new_recipient}})
        else:
            abort(400, description='Type the correct number')
    # event = events.find_one({'_id': event_id}) If he wants the event back or ok result
    
    return jsonify({'message' : 'Recipients have been added.'}), 200
