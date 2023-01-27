from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
event_ref = db.collection('events')

# Creating a blueprint instance for events
event_api = Blueprint('event_api',__name__)

@event_api.route('/')
def get_all_events():
    try:
        all_events = [doc.to_dict() for doc in event_ref.stream()]
        return jsonify(all_events),200
    except Exception as e:
        return f"An error occured: {e}"

        