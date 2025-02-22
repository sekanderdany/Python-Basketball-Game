import csv
from typing import List
from PlayerGameStats import PlayerGameStats
from Team import Team
from Player import Player
from Game import Game
from Tournament import Tournament


class Main:

    @staticmethod
    def main():
        # Call the create_tournament method to start the process
        tournament = Main.create_tournament()

        # Print tournament details
        Main.calculate_tournament_stats(tournament)

    # Create a tournament and populate its components
    @staticmethod
    def create_tournament():
        teams = Main.create_teams()
        players = Main.create_players(teams)

        # Create tournament
        tournament = Tournament(
            "Philadelphia 76ers at Los Angeles Lakers", "2001")

        # Add teams to the tournament
        for team in teams:
            tournament.add_team(team)

        # Create games and add to tournament
        games = Main.create_games(teams, players)
        for game in games:
            tournament.add_game(game)

        return tournament

    # Create and populate teams
    @staticmethod
    def create_teams():
        teams = []

        with open('e:/Documents & Learning/Python/Learn to code with Basketball/Step-4/TournamentData.csv', 'r') as file:
            # Extract team details from the CSV row
            reader = csv.DictReader(file)
            team_data = {}

            for row in reader:
                team_id = int(row['team_id'])
                team_name = row['team_name']
                conference = row['conference']

                # Check if the team is already added to the dictionary
                if team_id not in team_data:
                    team_data[team_id] = Team(team_id, team_name, conference)

            # Convert dictionary values to a list of teams
            teams = list(team_data.values())

        return teams

    # Create players and assign to teams
    @staticmethod
    def create_players(teams):
        players = []

        with open('e:/Documents & Learning/Python/Learn to code with Basketball/Step-4/TournamentData.csv', 'r') as file:
            reader = csv.DictReader(file)
            player_data = {}

            for row in reader:
                # Extract player details from the CSV row
                player_name = row['player_name']
                player_number = row['player_id']
                player_team_id = int(row['player_team_id'])

                # Check if the player is already added to the dictionary
                if player_number not in player_data:
                    # Create a Player object
                    player = Player(player_name, player_number)
                    player_data[player_number] = player

                    # Find the corresponding team and add the player to it
                    team = next((t for t in teams if t.get_id()
                                == player_team_id), None)
                    if team:
                        team.add_player(player)

            # Convert dictionary values to a list of players
            players = list(player_data.values())

        return players

    # Create games and add player stats
    @staticmethod
    def create_games(teams, players):
        games = []

        with open('e:/Documents & Learning/Python/Learn to code with Basketball/Step-4/TournamentData.csv', 'r') as file:
            reader = csv.DictReader(file)
            game_data = {}

            for row in reader:
                # Extract game and player stats from the CSV row
                game_id = int(row['game_id'])
                game_date = row['game_date']
                game_attendance = int(row['game_attendance'])
                game_home_team_id = int(row['game_home_team_id'])
                game_away_team_id = int(row['game_away_team_id'])
                player_name = row['player_name']
                player = next(
                    (p for p in players if p.get_name() == player_name), None)

                # Initialize the game data dictionary if the game_id is not already present
                if game_id not in game_data:
                    game_data[game_id] = {
                        'date': game_date,
                        'attendance': game_attendance,
                        'home_team': next((t for t in teams if t.get_id() == game_home_team_id), None),
                        'away_team': next((t for t in teams if t.get_id() == game_away_team_id), None),
                        'stats': []
                    }

                # Append player stats to the game data
                game_data[game_id]['stats'].append([
                    int(row['field_goals']),
                    int(row['three_points']),
                    int(row['free_throws']),
                    int(row['offensive_rebounds']),
                    int(row['defensive_rebounds']),
                    int(row['assists']),
                    player
                ])

        # Create Game objects and add player stats
        for game_id, data in game_data.items():
            home_team = data['home_team']
            away_team = data['away_team']
            if home_team is None or away_team is None:
                print(
                    f"Error: Missing team for game_id {game_id}. Home team: {home_team}, Away team: {away_team}. Skipping this game.")
                continue

            game = Game(game_id, data['date'],
                        home_team, away_team, data['attendance'])
            player_stats_list = PlayerGameStats.populate_player_game_stats(
                game, [s[-1] for s in data['stats']], data['stats'])
            Main.add_player_stats_to_game(game, player_stats_list)
            games.append(game)

        return games

    # Helper method to add player stats to the game
    @staticmethod
    def add_player_stats_to_game(game, player_stats_list):
        for stats in player_stats_list:
            # Add each player's stats to the game
            game.add_player_game_stats(stats)

    # Method to calculate and print tournament statistics
    @staticmethod
    def calculate_tournament_stats(tournament):
        # Print tournament details
        print("\nTournament: " + tournament.get_name())
        print("-------------------------------------------------------\n")

        games = tournament.get_games()

        # Calculate and print game-wise stats
        print("---Game-wise Stats---")

        for game in games:
            print("Game # " + str(game.get_game_number()) + ":")
            print(game.game_summary())
            print("-------------------------------------------------------\n")

            # Print highest scorers for each team
            Main.print_team_highest_scorers(game)
            print("-------------------------------------------------------\n")

        # Calculate and print the tournament winner and tournament-wise stats
        Main.print_tournament_winner_and_highest_scorer(tournament, games)

        # Display MVP stats
        Main.print_mvp_stats(tournament)
        print("-------------------------------------------------------\n")

    @staticmethod
    def print_team_highest_scorers(game):
        # Get the highest scorer for each team
        team_highest_scorer = game.highest_scorer()

        # Print the highest scorer for each team
        for team, scorer in team_highest_scorer.items():
            if scorer is not None:
                print("Team: " + team.get_name() +
                      ", Highest Scorer: " + scorer.get_name())
            else:
                print("Team: " + team.get_name() + ", Highest Scorer: None")

    # Method to print MVP stats
    @staticmethod
    def print_mvp_stats(tournament):
        # Get the MVP stats
        mvp_stats = tournament.mvp_stats(list(tournament.get_games()))

        # Print the MVP stats
        print("MVP Stats:")
        for key, value in mvp_stats.items():
            print("-- " + key + ": " + value)

    # Function to print tournament winner and highest scorer
    @staticmethod
    def print_tournament_winner_and_highest_scorer(tournament, games):
        # Get the tournament winner
        tournament_winner = tournament.get_tournament_winner()

        if tournament_winner:
            print("Tournament Winner: " + tournament_winner.get_name())
        else:
            print("The tournament ended in a draw.")

        # Get the highest scorer in the tournament
        highest_scorer = tournament.highest_scorer(games)

        if highest_scorer is not None:
            print("Highest Scorer of the Tournament: " +
                  highest_scorer.get_name())
        else:
            print("No player scored any points in the tournament.")


if __name__ == "__main__":
    Main.main()
