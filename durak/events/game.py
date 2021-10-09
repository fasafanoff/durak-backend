from flask import request
from flask_socketio import join_room, emit
import uuid
from durak.games import games


def search(game_name, number_of_players):
    game_type_id = game_name + str(number_of_players)
    if game_type_id not in games:
        games[game_type_id] = []
    games[game_type_id].append(request.sid)

    if len(games[game_type_id]) == number_of_players:
        room_id = uuid.uuid1()
        for _ in range(number_of_players):  
            sid = games[game_type_id].pop()
            join_room(room_id, sid=sid)
        emit('game_found', {'room_id': str(room_id)}, to=room_id)

# def game_ready(room_id):
