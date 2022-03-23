from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

import uuid
from user import user
from event import event

app = Flask(__name__)
CORS(app)
app.secret_key = 'mysecretkey'

app.register_blueprint(user, url_prefix="/api/users")
app.register_blueprint(event, url_prefix="/api/events")

 
if __name__ == '__main__':
    app.run(debug=True)
