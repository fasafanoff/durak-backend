class Rooms:
    def __init__(self):
        self.rooms = []

    def create_room(self, max_players, min_players, game_type):
        room = Room(max_players, min_players, game_type)
        self.rooms.append(room)

    def join_player(self, max_players, min_players, game_type):
        for room in self.rooms:
            if room.game_type != game_type:
                continue
            if room.player_should_join(min_players, max_players) and room.is_available():
                room.join("user")


class Room:
    ID_COUNTER = 0

    def __init__(self, max_players, min_players, game_type):
        self.max = max_players
        self.min = min_players
        self.game_type = game_type
        self.players = []
        self.room_id = Room.ID_COUNTER
        Room.ID_COUNTER += 1

    def is_available(self):
        number_of_player = len(self.players)
        if number_of_player < self.max:
            return True
        return False

    def player_should_join(self, min_players, max_players):
        return min_players <= self.min and max_players >= self.max

    def join(self, player):
        self.players.append(player)
