from durak.game.Pile import Pile


class Game:

    def __init__(self):
        self.deck_pile = Pile()
        self.rest_pile = Pile()
        self.players = []
