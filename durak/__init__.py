from dotenv import load_dotenv

from durak.Server import Server
from durak.events.game import search, connect

load_dotenv()


def create_app(test_config=None):
    server = Server(test_config)

    from .routes import auth
    server.add_route(auth.bp)

    server.add_event(search)
    server.add_event(connect)
    return server
