from flask import Blueprint, request, jsonify
from api import db

user_ref = db.collection('users')

# Creating a blueprint instance for users
user_api = Blueprint('user_api',__name__)

@user_api.route('/')
def get_all_users():
    try:
        all_users = [doc.to_dict() for doc in user_ref.stream()]
        return jsonify(all_users),200
    except Exception as e:
        return f"An error occured: {e}"

        
@user_api.route('/<user_id>')
def get_user(user_id):
    try:
        user = user_ref.document(user_id).get()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return f"An error occured: {e}"