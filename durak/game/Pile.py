from collections.abc import Iterable
from random import shuffle

class Pile:

    def __init__(self, pile=None):
        pile = pile or []
        self._pile = pile

    def get(self):
        return self._pile[:]

# TODO: understand why do I need add and remove
    def add(self, value):
        if isinstance(value, Iterable):
            self._pile.extend(value)
        else:
            self._pile.append(value)
        return self

    def moveto(self, other_pile, amount):
        self.__moveto_errors_checking(other_pile, amount)

        if amount == 0:
            return self

        split_point_index = len(self._pile) - amount
        moving_cards = self._pile[split_point_index:]
        other_pile.add(moving_cards)
        self._pile = self._pile[:split_point_index]
        return self

    def moveto_all(self, other_pile):
        self.__moveto_errors_checking(other_pile)
        other_pile.add(self._pile)
        self._pile.clear()

# TODO: not sure if this should be here
    def shuffle(self):
        shuffle(self._pile)

    def __len__(self):
        return len(self._pile)

    def __moveto_errors_checking(self, other_pile, amount=0):
        if self is other_pile:
            raise Exception("It's a dummy thing to move a pile to itself,\n you probably made a mistake!")

        if not isinstance(other_pile, Pile):
            raise Exception("other_pile should be an instance of a Pile class")

        if amount > self.__len__():
            raise Exception(f"Trying to move {amount} items from pile with length {self.__len__()}")

