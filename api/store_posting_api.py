from flask import Blueprint, request, jsonify
from api import db

store_posting_ref = db.collection('store_postings')

# Creating a blueprint instance for store postings
store_posting_api = Blueprint('store_posting_api',__name__)

@store_posting_api.route('/')
def get_all_store_postings():
    try:
        all_store_postings = [doc.to_dict() for doc in store_posting_ref.stream()]
        return jsonify(all_store_postings),200
    except Exception as e:
        return f"An error occured: {e}"

        