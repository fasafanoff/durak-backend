class Game:

    def __init__(self):
        self.table_pile = []
        self.deck = []
        self.players = []
        self.player_index = 0
        self.game_rules = {}

    def make_turn(self):
        player = self.players[self.player_index]
        self.game_rules.make_turn(player)
