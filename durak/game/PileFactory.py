from durak.game.Card import SuitRankCard
from durak.game.Pile import Pile


SUITS = ['SPADES', 'HEARTS', 'CLUBS', 'DIAMONDS']


class PileFactory:
    @staticmethod
    def create_36_deck():
        deck = []
        for suit in SUITS:
            for rank in range(6, 15):
                deck.append(SuitRankCard(suit, rank))
        return Pile(deck)
