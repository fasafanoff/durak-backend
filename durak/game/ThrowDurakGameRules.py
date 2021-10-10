from durak.game.Exceptions import NoCardInPlayersHand


class ThrowDurakGameRules:
    def __init__(self, desk=None, deck=None, rest=None, players=None):
        self.desk = desk or []
        self.deck = deck or []
        self.rest = rest or []
        self.players = players or []

    def throw(self, card):
        hand = self.players[0].hand
        if card not in hand:
            raise NoCardInPlayersHand(card, hand)

    def beat_throw(self, card):
        pass

    def take(self):
        pass

    def throw_after_take(self, cards):
        pass

    def skip(self):
        pass