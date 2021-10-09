import os
from flask import Flask
from flask_socketio import SocketIO


class Server:
    ws = None
    api = None

    def __init__(self, test_config=None):
        should_use_old_instance = Server.ws and Server.api
        if should_use_old_instance:
            return
        Server.api = Flask(__name__, instance_relative_config=True)
        Server.api.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(Server.api.instance_path, 'durak.sqlite'),
        )

        if test_config is None:
            Server.api.config.from_pyfile('config.py', silent=True)
        else:
            Server.api.config.from_mapping(test_config)

        try:
            os.makedirs(Server.api.instance_path)
        except OSError:
            pass

        from . import db
        db.init_app(Server.api)

        Server.ws = SocketIO(Server.api)

    @staticmethod
    def add_route(route):
        Server.api.register_blueprint(route)

    @staticmethod
    def add_event(callback, event_name=None):
        if event_name is None:
            Server.ws.event(callback)
        else:
            Server.ws.on(event_name)(callback)
