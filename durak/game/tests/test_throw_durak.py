from durak.game.Card import SuitRankCard
from durak.game.Exceptions import NoCardInPlayersHand
from durak.game.ThrowDurakGameRules import ThrowDurakGameRules
from pytest import fixture, raises


class DummyPlayer:
    def __init__(self, hand=None):
        self.hand = hand or []


@fixture
def full_players():
    hand1 = []
    hand2 = []
    for i in range(6):
        hand1.append(SuitRankCard(SuitRankCard.DIAMONDS, i + 6))
        hand2.append(SuitRankCard(SuitRankCard.SPADES, i + 6))
    return [DummyPlayer(hand1), DummyPlayer(hand2)]


def test_game_rules_validation(full_players):
    game_rules = ThrowDurakGameRules(players=full_players)
    with raises(NoCardInPlayersHand):
        game_rules.throw(SuitRankCard(SuitRankCard.CLUBS, 10))