import pytest

from durak.game.Exceptions import AttackingPlayerOutOfBoundary
from durak.game.PlayersTurnManager import PlayersTurnManager


def test_queue_attacking_player_index_set():
    with pytest.raises(AttackingPlayerOutOfBoundary):
        PlayersTurnManager([1, 2, 3, 4], attacking_player_index=5)


@pytest.fixture
def player_queue():
    yield PlayersTurnManager([1, 2, 3, 4])


def test_get_methods_of_player_queue(player_queue):
    assert player_queue.get_attacker() == 1
    assert player_queue.get_current() == 1
    assert player_queue.get_defender() == 2


def test_change_attacker_should_change_player_to_next(player_queue):
    player_queue.change_attacker()
    assert player_queue.get_attacker() == 2
    assert player_queue.get_defender() == 3


def test_change_thrower_after_second_change_current_should_be_after_defender(player_queue):
    player_queue.change_thrower()
    assert player_queue.get_current() == 3


def test_change_thrower_should_change_attacker_after_looping(player_queue):
    player_queue.change_thrower()
    player_queue.change_thrower()
    player_queue.change_thrower()
    assert player_queue.get_attacker() == 2


def test_change_thrower_should_not_change_attacker(player_queue):
    player_queue.change_thrower()
    player_queue.change_thrower()
    player_queue.should_not_change_attacker()
    player_queue.change_thrower()
    assert player_queue.get_attacker() == 1

