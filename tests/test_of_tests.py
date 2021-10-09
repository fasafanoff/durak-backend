import json
import unittest

from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace, disconnect




def test():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    socketio = SocketIO(app)

    @socketio.on('join')
    def on_join_room(a):
        join_room('room')

    client1 = socketio.test_client(app, flask_test_client=app.test_client())
    client1.emit('join','durak')
    assert False

