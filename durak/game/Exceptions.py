class InvalidMoveType(Exception):
    def __init__(self, move_type):
        self.move_type = move_type
        super().__init__(f"No move type {move_type} was found in mappings")


class NoCardInPlayersHand(Exception):
    def __init__(self, card, hand):
        self.card = card
        self.hand = hand
        super().__init__(f"{self.card} was not found in {self.hand}")
