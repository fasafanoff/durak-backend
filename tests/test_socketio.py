

def test_search_with_no_authentication_to_guest_queue(socketio_client):
    socketio_client.emit('search')



