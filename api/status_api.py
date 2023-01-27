from flask import Blueprint, request, jsonify
from api import db
from firebase_admin import db as database

status_ref = database.reference('status')

# Creating a blueprint instance for tournamnets
status_api = Blueprint('status_api', __name__)


@status_api.route('/')
def get_all_status():
    try:
        all_status = status_ref.get()
        return jsonify(all_status), 200
    except Exception as e:
        return f"An error occured: {e}"
