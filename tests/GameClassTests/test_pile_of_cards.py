from durak.game.Pile import Pile
import pytest


def test_pile_modifying_returned_array_from_get_should_not_change_the_original_pile():
    pile = Pile([1, 2, 3])
    arr = pile.get()
    arr.clear()
    assert len(pile) is 3


def test_pile_len_should_return_the_length_of_the_pile():
    assert len(Pile()) is 0
    assert len(Pile([1, 2, 3])) is 3
    assert len(Pile([1])) is 1


def test_pile_add_should_increase_the_length_accordingly():
    assert len(Pile().add(1)) is 1
    assert len(Pile([1, 2, 3]).add((1, 2))) is 5
    assert len(Pile([1]).add([1])) is 2


def test_pile_moveto_should_decrease_the_length_of_one_pile_and_increase_the_other_one():
    pile1 = Pile([1, 2, 3])
    pile2 = Pile([4, 5, 6])
    pile1.moveto(pile2, 2)
    assert len(pile1) is 1
    assert len(pile2) is 5


def test_pile_moveto_throws_an_exception_if_dummy_input_is_provided():
    pile1 = Pile([1, 3, 3])
    with pytest.raises(Exception):
        assert pile1.moveto(pile1, 2)
        assert pile1.moveto(None, 2)
        assert pile1.moveto([], 2)


def test_pile_moveto_all():
    pile1 = Pile([1, 2, 3])
    pile2 = Pile([4, 5, 6])
    pile1.moveto_all(pile2)
    assert len(pile1) is 0
    assert len(pile2) is 6


def test_pile_moveto_throws_an_exception_if_there_are_less_cards_then_passed_to_amount():
    pile1 = Pile([1, 3, 3])
    pile2 = Pile([1, 3, 3, 5, 6, 7])

    with pytest.raises(Exception):
        assert pile1.moveto(pile2, 4)
