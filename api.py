import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello World"

cred = credentials.Certificate("serviceaccountkey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://clipboard-c6b51-default-rtdb.firebaseio.com/'
})


@app.route('/api', methods=['GET'])
def api():
    if request.method == 'GET':
        
        ref = db.reference('/')

        # read ref as json data
        snapshot = ref.order_by_key().get()

        # reverse the ordered dict by key to get the latest data
        snapshot = dict(reversed(list(snapshot.items())))

        print(snapshot)

        return jsonify(snapshot)


@app.route('/api', methods=['POST'])
def api_post():
    if request.method == 'POST':
        # check if the post request has the json data
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        
        # get the json data

        data = request.get_json()
        
        print(data)

        ref = db.reference('/')
        ref.push(data)
        return jsonify(data)
