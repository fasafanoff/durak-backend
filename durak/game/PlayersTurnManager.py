from durak.game.Exceptions import AttackingPlayerOutOfBoundary


class PlayerQueue:
    def __init__(self, players, reverse=False, attacking_player_index=0):

        if attacking_player_index >= len(players):
            raise AttackingPlayerOutOfBoundary(players, attacking_player_index)

        self.players = players
        self.number_of_players = len(players)

        # indexes
        self._current_thrower = self._attacking_player = attacking_player_index
        self._defending_player = self._move_array_index(
            attacking_player_index, reverse=reverse
        )

        self._reverse = reverse

    def change_thrower(self):
        self._change_to_next_thrower()
        if self._is_no_throwers_left():
            self._change_to_next_attacker()

    def change_attacker(self):
        self._change_to_next_attacker()

    def restart_thrower(self):
        pass

    def get_attacker(self):
        return self.players[self._attacking_player]

    def get_defender(self):
        return self.players[self._defending_player]

    def _change_to_next_thrower(self):
        self._current_thrower = self._increment_forward_with_wrap(self._current_thrower)

    def _is_no_throwers_left(self):
        return self._current_thrower == self._defending_player

    def _increment_forward_with_wrap(self, value):
        return self._move_array_index(value, reverse=self._reverse)

    def _decrement_forward_with_wrap(self, value):
        return self._move_array_index(value, reverse=not self._reverse)

    def _move_array_index(self, value, reverse=False):
        if reverse:
            new_value = value - 1
        else:
            new_value = value + 1
        return new_value % self.number_of_players

    def _change_to_next_attacker(self):
        self._current_thrower = self._attacking_player \
            = self._increment_forward_with_wrap(self._attacking_player)
        self._defending_player = self._decrement_forward_with_wrap(self._attacking_player)

