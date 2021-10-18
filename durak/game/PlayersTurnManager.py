from durak.game.Exceptions import AttackingPlayerOutOfBoundary


class PlayersTurnManager:
    def __init__(self, players, attacking_player_index=0):
        if attacking_player_index >= len(players):
            raise AttackingPlayerOutOfBoundary(players, attacking_player_index)

        self.players = players
        self.number_of_players = len(players)
        self.should_change_attacker = True
        self.current = self.attacker = attacking_player_index
        self.defender = self._wrap_increment(self.attacker)

    def change_thrower(self) -> None:
        if self._is_current_thrower_first():
            return self._make_current_next_player_after_defender()
        if self._is_current_thrower_last() and self.should_change_attacker:
            return self._change_attacker()
        self._make_current_next_player()

    def should_not_change_attacker(self):
        self.should_change_attacker = False

    def change_attacker(self):
        self._change_attacker()

    def get_attacker(self):
        return self.players[self.attacker]

    def get_defender(self):
        return self.players[self.defender]

    def get_current(self):
        return self.players[self.current]

    def _wrap_increment(self, value):
        return (value + 1) % self.number_of_players

    def _wrap_decrement(self, value):
        return (value - 1) % self.number_of_players

    def _change_attacker(self):
        self.current = self.attacker = self._wrap_increment(self.attacker)
        self.defender = self._wrap_increment(self.attacker)

    def _is_current_thrower_last(self):
        return self.current == self._wrap_decrement(self.attacker)

    def _is_current_thrower_first(self):
        return self.current == self.attacker

    def _make_current_next_player_after_defender(self):
        self.current = self._wrap_increment(self.defender)

    def _make_current_next_player(self):
        self.current = self._wrap_increment(self.current)
