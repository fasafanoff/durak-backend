class SocketioClients:
    def __init__(self, socketio_app, app, client):
        self.socketio_app = socketio_app
        self.app = app
        self.client = client

    def get(self):
        return self.socketio_app.test_client(
            self.app, flask_test_client=self.client)

    def get_tuple(self, amount=1):
        return (self.get() for _ in range(amount))
