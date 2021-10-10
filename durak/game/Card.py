
class SuitRankCard:
    DIAMONDS = 'DIAMONDS'
    SPADES = 'SPADES'
    CLUBS = 'CLUBS'
    HEARTS = 'HEARTS'

    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
