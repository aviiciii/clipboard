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

def generate_key(latest_value):
    return int(latest_value) + 1 if latest_value else 1

@app.route('/api', methods=['GET'])
def api():
    if request.method == 'GET':
        
        ref = db.reference('/')

        # read ref as json data
        snapshot = ref.order_by_key().get()

        
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

        # get the clipboard data
        clip = data['body']
        print(clip)

        # get the database reference
        ref = db.reference('/')

        # read ref as json data
        snapshot = ref.order_by_key().get()

        # reverse the ordered dict by key to get the latest data
        snapshot = dict(reversed(list(snapshot.items())))
        latest_key = list(snapshot.keys())[0]
        print(latest_key)

        # get new key
        new_key = generate_key(latest_key)
        print(new_key)

        # new clipboard data
        new_clip = {'data': clip}
        new_clip = json.dumps(new_clip)
        # get the database reference
        ref = db.reference('/')
        
        # update the database
        ref.child(str(new_key)).set({
            'data': clip
        })

        return jsonify(data)
