from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import uuid
from user import user
from event import event

app = Flask(__name__)

app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(event, url_prefix="/events")

if __name__ == '__main__':
    app.run(debug=True)
