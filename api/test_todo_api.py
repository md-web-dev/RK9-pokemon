from flask import Blueprint, request, jsonify
from api import db


todo_ref = db.collection('test-todos')

# Creating a blueprint instance for test todos
todo_api = Blueprint('todo_api',__name__)

@todo_api.route('/')
def get_all_todos():
    """
      get_all_todos() : Fetches all todo documents from Firestore collection as JSON.
      all_todos : Return all documents.
    """
    try:
        all_todos = [doc.to_dict() for doc in todo_ref.stream()]
        return jsonify(all_todos),200
    except Exception as e:
        return f"An error occured: {e}"

@todo_api.route('/<todo_id>')
def get_todo(todo_id):
    print(todo_id)
    try:        
        todo = todo_ref.document(todo_id).get()
        return jsonify(todo.to_dict()), 200
    except Exception as e:
        return f"An error occured: {e}"