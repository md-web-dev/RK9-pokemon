from flask import Blueprint, request, jsonify
from api import db
from firebase_admin import db as database

counter_ref = database.reference('counters')

# Creating a blueprint instance for tournamnets
counter_api = Blueprint('counter_api', __name__)


@counter_api.route('/')
def get_all_counters():
    try:
        all_counters = counter_ref.get()
        return jsonify(all_counters), 200
    except Exception as e:
        return f"An error occured: {e}"
