from durak.game.PlayerQueue import PlayerQueue


def test_queue_two_players():
    player_queue = PlayerQueue([1, 2])
    player_queue.change_thrower()
    assert player_queue.get_attacker() == 2
    assert player_queue.get_defender() == 1
