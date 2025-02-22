'''
Let’s start with the Player class.

As you'll see, the code for this class is not noteworthy complex. The only notable aspect is our use of list in the Player number and main (line 4) classes to compile the player roster.

Properties
-----------
The Player class will have the following properties:

name: This is the name of the player.

number: This is the number of the player that is associated with a player.

Methods
-------
populate_players: This function will populate players in the class.

print_player: This function prints data about each player.

Challenge
This lesson’s task is to display the player’s name and number on the console. To facilitate the beginning, almost the complete code and the method for populating players in the class have been provided.

Your task here is to:

Call the populate_player in the main class so players get populated.

Write a function to print players data on the console.

Input
For populate_players method, we have a predefined list of lists containing the following data:

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

Required output
The output of this challenge should look like the following:

Player Name: Allen Iverson, Player Number: 1
Player Name: Aaron McKie, Player Number: 2
Player Name: Dikembe Mutombo, Player Number: 3
Player Name: Tyrone Hill, Player Number: 4
Player Name: Jumaine Jones, Player Number: 5
Player Name: Kobe Bryant, Player Number: 6
Player Name: Shaquille O'Neal, Player Number: 7
Player Name: Rick Fox, Player Number: 8
Player Name: Horace Grant, Player Number: 9
Player Name: Derek Fisher, Player Number: 10

Explanation
In the Player.py file:
Lines 1–4: Define the Player class and initializes name and number attributes.

Lines 7–11: Methods get_name and get_number return the player’s name and number, respectively.

Lines 14–21: The populate_players method is responsible for creating a list of Player objects from a given list of player data. It iterates over each element in player_data, creates a Player object for each, and adds it to the players list. Finally, it returns the list.

Lines 23–25: The print_player method prints the player’s name and number.

In the main.py file:
Line 1: Import the Player class.

Lines 3–4: Define a class Main with a static list players to store player data.

Lines 6–10: The main method is the entry point of the program. It calls create_players() to generate a list of players and then calls print_players(players) to print information about the created players.

Lines 12–31: The create_players method contains predefined player data as a list of lists. It calls the Player.populate_players(player_data) method to create a list of Player objects from this data and returns the list.

Lines 34–36: The print_players method iterates over the list of Player objects and calls the print_player method on each one, printing their names and numbers.
'''