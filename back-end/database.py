from pymongo import MongoClient
import os

uri = os.environ.get('MONGODB_URI')
client = MongoClient(uri)
db = client.Colab8
users = db.users
users.create_index("phone_number", unique = True)
contacts = db.contacts
events = db.events