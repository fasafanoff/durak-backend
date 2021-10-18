import pytest

from durak.game.Exceptions import AttackingPlayerOutOfBoundary
from durak.game.PlayerQueue import PlayerQueue


def test_queue_two_players():
    player_queue = PlayerQueue([1, 2])
    player_queue.change_thrower()
    assert player_queue.get_attacker() == 2
    assert player_queue.get_defender() == 1


def test_queue_change_attacker():
    player_queue = PlayerQueue([1, 2, 3, 4])
    player_queue.change_thrower()
    player_queue.change_attacker()
    assert player_queue.get_attacker() == 3
    assert player_queue.get_defender() == 2


def test_queue_direction_change_change_attacker():
    player_queue = PlayerQueue([1, 2, 3, 4], reverse=False)
    player_queue.change_attacker()
    assert player_queue.get_attacker() == 4
    assert player_queue.get_defender() == 1


def test_queue_attacking_player_index_set():
    with pytest.raises(AttackingPlayerOutOfBoundary):
        PlayerQueue([1, 2, 3, 4], attacking_player_index=5)


def test_queue_attacking_player_index():
    player_queue = PlayerQueue([1, 2, 3, 4],  attacking_player_index=2)
    assert player_queue.get_attacker() == 3
    assert player_queue.get_defender() == 4

