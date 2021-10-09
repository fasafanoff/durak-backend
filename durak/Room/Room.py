class Allowance:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Room:
    def __init__(self, password, game_type, allowance):
        self.password = password
        self.game_type = game_type
        self.allowance = allowance or Allowance()

    def can_join(self, player):
        if self.password is not player.password:
            return False

        return self.allowance.test(player)

