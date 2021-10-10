from durak.game.Exceptions import InvalidMoveType


class Game:
    def __init__(self, game_rules):
        self.game_rules = game_rules()

    def make_move(self, move_type, args=None):
        args = args or {}
        move_types = self.game_rules.mappings
        if move_type not in move_types:
            raise InvalidMoveType(move_type)
