from durak.game.Pile import Pile
from durak.game.PileFactory import PileFactory


class Game:

    def __init__(self, players):
        self.players = players
        self.rest_pile = PileFactory.create_36_deck()
        for player in players:
            self.rest_pile.moveto(player.hand_pile, 6)

        self.used_pile = Pile()
        self.desk_pile = Pile()

