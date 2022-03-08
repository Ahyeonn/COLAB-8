from pymongo import MongoClient

client = MongoClient()
db = client.Colab8
users = db.users
users.create_index("phone_number", unique = True)
events = db.events
