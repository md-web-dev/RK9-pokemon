from flask import Blueprint, request, jsonify
from api import db
from firebase_admin import db as database

tournament_ref = database.reference('tournaments')

# Creating a blueprint instance for tournamnets
tournament_backup_api = Blueprint('tournament_backup_api', __name__)


@tournament_backup_api.route('/')
def get_all_tournaments():
    try:
        all_tournaments = tournament_ref.get()
        return jsonify(all_tournaments), 200
    except Exception as e:
        return f"An error occured: {e}"