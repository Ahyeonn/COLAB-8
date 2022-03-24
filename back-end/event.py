from flask import Blueprint, request, jsonify, abort
from bson.objectid import ObjectId
from twilio_api import create_rsvp
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
    new_event = {
      '_id':        request.json['event_id'],
      'owner_id':   request.json['owner_id'] or None,
      'name':       request.json['name'],
      'event_name': request.json['event_name'],
      'host_phone': request.json['host_number'],
      'date':       request.json['date'],
      'time':       request.json['time'],
      'recipients': []
    }

    event_id = events.insert_one(new_event).inserted_id
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
    event_rsvps = rsvps.find({'event_id': event_id})
    if event:
        return jsonify({'event result' : [event, rsvps]}), 200
    abort(404, description='not found')

@event.route('/rsvp', methods=['POST'])
def send_users_rsvp():
    recipients = request.json['contacts']
    event_id = request.json['contacts']['event_id']
    for recipient in recipients:
        new_recipient = {
            'name': recipient['name'],
            'phone_number': recipient['phoneNumber']
        }
        events.update_one({'_id': event_id}, {'$push':{'recipients': new_recipient}})

    # event = events.find_one({'_id': event_id}) If he wants the event back or ok result
    
    return jsonify({'message' : 'Recipients have been added.'}), 200
