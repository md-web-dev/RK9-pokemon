from flask import Blueprint, request, jsonify
from api import db
from firebase_admin import db as database

tournament_type_ref = database.reference('tournament_type')

# Creating a blueprint instance for tournamnets
tournament_type_api = Blueprint('tournament_type_api', __name__)


@tournament_type_api.route('/')
def get_all_tournament_types():
    try:
        all_tournament_types = tournament_type_ref.get()
        return jsonify(all_tournament_types), 200
    except Exception as e:
        return f"An error occured: {e}"
