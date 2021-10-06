from durak.game.Game import Game
from durak.game.Player import Player


def test_all_piles_length():
    players = [Player(), Player()]
    game = Game(players)

    assert len(game.used_pile) == 0
    assert len(game.desk_pile) == 0
    assert len(game.rest_pile) == 36 - 2 * 6

    assert len(game.players[0].hand_pile) == 6
    assert len(game.players[1].hand_pile) == 6
