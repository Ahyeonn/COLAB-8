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
      'host_number': request.json['host_number'],
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
    event_id = request.json['event_id']
    for recipient in recipients:
        create_rsvp(recipient, event_id)
    
    return jsonify({'message' : 'Recipients have been added.'}), 200

# Ask for yes / no response
@event.route('/rsvp/<rsvp_id>', methods=['POST'])
def event_response(rsvp_id):
    rsvp = rsvps.find_one({'_id': rsvp_id})

    if not rsvp:
        return jsonify({'message' : 'Invitation is expired or invalid.'})

    event = events.find_one({'_id': rsvp['event_id']})

    response = True if request.json['response'] == 'true' else False

    rsvps.update_one({'_id': rsvp_id}, {'$set':{'status': response}})

    return jsonify({'message' : 'Thank you for your response! You may close this page'})