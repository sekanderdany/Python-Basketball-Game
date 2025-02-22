from Player import Player


class Main:
    players = []  # This initializes the players list

    def main():
        players = Main.create_players()

        # Print the players
        Main.print_players(players)

    def create_players():
        # Players data
        player_data = [
            ["Allen Iverson", "1"],
            ["Aaron McKie", "2"],
            ["Dikembe Mutombo", "3"],
            ["Tyrone Hill", "4"],
            ["Jumaine Jones", "5"],
            ["Kobe Bryant", "6"],
            ["Shaquille O'Neal", "7"],
            ["Rick Fox", "8"],
            ["Horace Grant", "9"],
            ["Derek Fisher", "10"]
        ]

        # Populate players list
        players = Player.populate_player(player_data)

        # Return players list
        return players

    # Helper method to print players
    def print_players(players):
        for player in players:
            player.print_player()


# Main execution
if __name__ == "__main__":
    Main.main()
