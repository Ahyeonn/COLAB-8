from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from database import *
import uuid

contact = Blueprint("contact", __name__)

# Contact
@contact.route('/', methods=['GET'])
def get_events():
    output = []
    for event in events.find():
        output.append({'name' : event['name'], 'meeting_name': event['meeting_name'], 'date': event['date'], 'time': event['time']})

    return jsonify({'meeting result' : output})

@contact.route('/<meeting_id>', methods=['GET'])
def get_single_event(meeting_id):
    event = events.find_one({'_id': meeting_id})

    if event:
        output = event
    else:
        output = 'event is not found'
    
    return jsonify({'event result' : output})

@contact.route('/', methods=['POST'])
def add_contact():
    output = []
    phone_number = request.json['phone_number']
    # way to iterate the page? like press add contact number gives one mor contact_number +1 to our variable name?
    contact_number = request.json['contact_number']
    contact_number2 = request.json['contact_number2']
    contact_number3 = request.json['contact_number3']
    if len(request.json) > 4:
        count = 1
        for i in request.json:
            count += 1
            if count > 4:
                
                print(request.json[i])
    # for number in (len(request.json)-1):
        
    # for idx in (len(request.json)-1):
    #     set contact_number(idx) = request.json['phone_number(idx)']

    # event_id = events.insert_one({'_id': uuid.uuid4().hex, 'name': name, 'meeting_name': meeting_name, 'date': date, 'time': time }).inserted_id
    # find_event = events.find_one({'_id' : event_id})
    # return jsonify(find_event)
    return jsonify({'contact result' : output})
    # contact_id
