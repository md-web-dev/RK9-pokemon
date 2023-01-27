import os
from flask import Flask
from firebase_admin import credentials, initialize_app, firestore, db as database

cred = credentials.Certificate(
    f'{os.getcwd()}/rk9-project-2-dev-7b6c85a1af26-jellis-RO.json')
default_app = initialize_app(
    cred, {"databaseURL": "https://rk9-project-2-dev.firebaseio.com"})
db = firestore.client()


def create_app():
    app = Flask(__name__)

    from .user_api import user_api
    from .test_todo_api import todo_api
    from .tournament_api import tournament_api
    from .event_api import event_api
    from .store_posting_api import store_posting_api
    from .tournament_backup_api import tournament_backup_api

    from .tournament_type_api import tournament_type_api
    from .status_api import status_api
    from .counter_api import counter_api 
    from .backup_api import backup_api   

    # Firestore routes
    app.register_blueprint(user_api, url_prefix='/users')
    app.register_blueprint(todo_api, url_prefix='/todos')
    app.register_blueprint(tournament_api, url_prefix='/tournaments')
    app.register_blueprint(event_api, url_prefix='/events')
    app.register_blueprint(store_posting_api, url_prefix='/store-postings')

    # Realtime database routes
    app.register_blueprint(tournament_backup_api,
                           url_prefix='/tournaments-backup')
    app.register_blueprint(tournament_type_api, url_prefix='/tournaments-type')
    app.register_blueprint(status_api, url_prefix='/status')
    app.register_blueprint(counter_api, url_prefix='/counters')
    app.register_blueprint(backup_api, url_prefix='/backup')

    return app
