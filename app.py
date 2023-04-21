import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import os

# from dotenv import load_dotenv

# load_dotenv()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello World"
# Fetch the service account key JSON file contents
service_key = json.loads(os.environ['SERVICE_ACCOUNT_KEY'])
cred = credentials.Certificate(service_key)

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

        # read ref as json data to a list
        snapshot = ref.order_by_key().get()

        # remove null in snapshot list
        snapshot = list(filter(None, snapshot))
        
        # create a dict to store the clipboard data
        clipboard = {}

        # refactor the data to a dict
        for clip in range(len(snapshot)):
            clipboard[clip+1] = snapshot[clip]['data']


        return jsonify(clipboard)


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
