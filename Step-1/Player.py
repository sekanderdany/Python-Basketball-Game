class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    # Getters
    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    # Method to populate players
    def populate_player(player_data):
        players = []
        for data in player_data:
            name = data[0]
            number = int(data[1])
            player = Player(name, number)
            players.append(player)
        return players

    # Method to print a single player
    def print_player(self):
        print(
            f"Player Name: {self.get_name()}, Player Number: {self.get_number()}")
