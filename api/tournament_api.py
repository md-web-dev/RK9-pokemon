from flask import Blueprint, request, jsonify
from api import db

tournament_ref = db.collection('tournaments')

# Creating a blueprint instance for tournamnets
tournament_api = Blueprint('tournament_api',__name__)

@tournament_api.route('/')
def get_all_tournaments():
    try:
        all_tournaments = [doc.to_dict() for doc in tournament_ref.stream()]        
        return jsonify(all_tournaments),200        
    except Exception as e:
        return f"An error occured: {e}"

        