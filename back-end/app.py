from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import uuid
from user import user
from event import event
from contact import contact

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config["APPLICATION_ROOT"] = "/api"

app.register_blueprint(user, url_prefix="/users")
app.register_blueprint(event, url_prefix="/events")
# app.register_blueprint(contact, url_prefix="/contacts")

 
if __name__ == '__main__':
    app.run(debug=True)
