class PlayerQueue:
    def __init__(self, players):
        self.players = players
        self.number_of_players = len(players)

        # indexes
        self.attacking_player = 0
        self.current_thrower = 0
        self.defending_player = 1

    def change_thrower(self):
        self._change_to_next_thrower()
        if self._is_no_throwers_left():
            self._change_to_next_attacker()

    def restart_thrower(self):
        pass

    def get_attacker(self):
        return self.players[self.attacking_player]

    def get_defender(self):
        return self.players[self.defending_player]

    def _increment_with_wrap(self, value):
        return (value + 1) % self.number_of_players

    def _change_to_next_thrower(self):
        self.current_thrower = self._increment_with_wrap(self.current_thrower)

    def _is_no_throwers_left(self):
        return self.current_thrower == self.defending_player

    def _change_to_next_attacker(self):
        self.current_thrower = self.attacking_player \
            = self._increment_with_wrap(self.attacking_player)
        self.defending_player = self._increment_with_wrap(self.attacking_player)

