from unittest.mock import patch


def test_durak_should_emit_game_found_event(socketio_clients):
    client1, client2 = socketio_clients.get_tuple(2)

    client1.emit('search', 'durak', 2)
    client2.emit('search', 'durak', 2)

    client1_events = client1.get_received()
    client2_events = client2.get_received()
    assert len(client1_events)
    assert len(client2_events)

    client1_event = client1_events.pop()
    client2_event = client2_events.pop()

    assert client1_event is not None
    assert client2_event is not None

    assert client1_event['name'] == client2_event['name'] == 'game_found'


def test_durak_should_not_emit_game_found_event_for_three(socketio_clients):
    client1, client2 = socketio_clients.get_tuple(2)

    client1.emit('search', 'durak', 3)
    client2.emit('search', 'durak', 3)

    client1_events = client1.get_received()
    client2_events = client2.get_received()

    assert not len(client1_events)
    assert not len(client2_events)


def test_durak_should_not_emit_game_found_event_different_number_of_players(socketio_clients):
    client1, client2 = socketio_clients.get_tuple(2)

    client2.emit('search', 'durak', 3)
    client1.emit('search', 'durak', 2)

    client1_events = client1.get_received()
    client2_events = client2.get_received()

    assert not len(client1_events)
    assert not len(client2_events)


def test_durak_should_return_correct_room_id_when_game_is_found(socketio_clients):
    CORRECT_ROOM_ID = 'correct room id'

    with patch('uuid.uuid1') as uuid:
        uuid.return_value = CORRECT_ROOM_ID

        client1, client2 = socketio_clients.get_tuple(2)

        client2.emit('search', 'durak', 2)
        client1.emit('search', 'durak', 2)

        client1_events = client1.get_received().pop()
        client2_events = client2.get_received().pop()

        assert client1_events['args'][0]['room_id'] == CORRECT_ROOM_ID

        assert client2_events['args'][0]['room_id'] == CORRECT_ROOM_ID
