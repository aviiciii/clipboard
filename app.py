# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# Json, OS and Flask
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
# Enable CORS
CORS(app)


# Fetch the service account key JSON file contents
service_key = json.loads(os.environ['SERVICE_ACCOUNT_KEY'])
cred = credentials.Certificate(service_key)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://clipboard-c6b51-default-rtdb.firebaseio.com/'
})




@app.route('/', methods=['GET'])
def home():
    return "Hello World"



@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        
        ref = db.reference('/')

        # read ref as json data to a list
        snapshot = ref.order_by_key().get()

        clipboard = generate_clipboard(snapshot)

        if not clipboard:
            return jsonify({"msg": "No data found in the database."}), 404

        return jsonify(clipboard)

    elif request.method == 'POST':
        # check if the post request has the json data
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        
        # get the content from the json data
        data = request.get_json()
        clip = data['body']

        print(clip)

        # get the database reference
        ref = db.reference('/')

        # read ref as json data
        snapshot = ref.order_by_key().get()

        # generate clipboard data
        clipboard = generate_clipboard(snapshot)

        # get new key
        new_key = generate_key(clipboard)
        print(new_key)

        try:
            # update the database
            ref.child(str(new_key)).set({
                'data': clip
            })
        except:
            return jsonify({"msg": "Error while updating the database. Try again. Contact developer if problem persists at https://github.com/aviiciii ."}), 500

        return jsonify({"msg": "Data added to the database."}), 200

    else:
        return jsonify({"msg": "Method not allowed. The '/api' route accepts only GET and POST."}), 405

# Generate new key
def generate_key(clipboard):
    if not clipboard:
        return 1
    else:
        latest_key = max(clipboard.keys())
    return int(latest_key) + 1 if latest_key else 1

# Error handler

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"msg": "Page not found. Try '/api' route for requests. Contact developer at https://github.com/aviiciii ."}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"msg": "Internal server error. Raise issue at https://github.com/aviiciii/clipboard/issues ."}), 500

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"msg": "Method not allowed. The '/api' route accepts only GET and POST."}), 405

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"msg": "Bad request"}), 400

@app.errorhandler(403)
def forbidden(e):
    return jsonify({"msg": "Forbidden"}), 403








# Generate clipboard data from the database
def generate_clipboard(snapshot):

    if not snapshot:
        return {}

    # remove null in snapshot list
    snapshot = list(filter(None, snapshot))
    
    # create a dict to store the clipboard data
    clipboard = {}

    # refactor the data to a dict
    for clip in range(len(snapshot)):
        clipboard[clip+1] = snapshot[clip]['data']

    return clipboard