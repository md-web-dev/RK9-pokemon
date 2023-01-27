from flask import Blueprint, request, jsonify
from api import db
from firebase_admin import db as database

backup_ref = database.reference('backup')

# Creating a blueprint instance for tournamnets
backup_api = Blueprint('backup_api', __name__)


@backup_api.route('/')
def get_all_backups():
    try:
        all_backups = backup_ref.get()
        return jsonify(all_backups), 200
    except Exception as e:
        return f"An error occured: {e}"
