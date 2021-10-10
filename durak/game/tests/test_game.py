from durak.game.Exceptions import InvalidMoveType
from durak.game.Game import Game
import pytest


class GameRules:
    def __init__(self):
        self.mappings = {
            'throw': self.throw,
        }

    def throw(self):
        pass


def test_game_no_event():
    game = Game(game_rules=GameRules)
    with pytest.raises(InvalidMoveType):
        game.make_move('throw1')

