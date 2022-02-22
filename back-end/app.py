from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.Colab8
comments = db.comments

@app.route('/hello/<string:name>/')
def comments_index(name):
    """Show all comments"""
    response = {'msg': 'Hello {}'.format(name)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

