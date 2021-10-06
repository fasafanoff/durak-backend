from durak.game.PileFactory import PileFactory


def test_36_deck_should_have_36_length():
    deck36 = PileFactory.create_36_deck()
    assert len(deck36) == 36
