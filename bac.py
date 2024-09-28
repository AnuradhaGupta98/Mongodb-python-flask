from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

# Create Flask app with static files in the 'assets' folder
app = Flask(__name__, static_folder='static', static_url_path='/')
CORS(app)

# Connect to MongoDB Atlas
mongo_uri = "mongodb+srv://guptaanuradha4498:U1toT5QSsnRzeT6J@clustertest.la9lc.mongodb.net/personal_db?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client['personal_db']
collection = db['personal_details']

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')  # Assuming index.html is inside 'assets'

@app.route('/records', methods=['POST'])
def add_record():
    data = request.json
    record_id = collection.insert_one(data).inserted_id
    return jsonify({'id': str(record_id)})

if __name__ == '__main__':
    app.run(debug=True)
