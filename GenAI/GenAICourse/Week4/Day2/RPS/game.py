#Game - This will contain a game class that has the functions to play a single game of rock-paper-scissors 
#against the computer, determine the result, and return the result.

import random

class Game:
    def get_user_item(self):
        """Ask the user to select an item and validate input."""
        valid_choices = ['rock', 'paper', 'scissors']
        while True:
            choice = input("Select an item (rock/paper/scissors): ").strip().lower()
            if choice in valid_choices:
                return choice
            print("Invalid input. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """Selects rock, paper, or scissors at random for the computer."""
        valid_choices = ['rock', 'paper', 'scissors']
        return random.choice(valid_choices)
    
    def get_game_result(self, user_item, computer_item):
        """Determines if the user won, low, or drew against the computer."""
        if user_item == computer_item:
            return "draw"
        
        #A dictionary defining what beast what (Key beats Value)
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if winning_combinations[user_item] == computer_item:
            return "win"
        else:
            return "loss"
        
    def play(self):
        """Executes a single game, prints the output, and returns the result."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        #Format the grammar of the output message based on the result.
        if result == "Draw!":
            outcome_message = "You drew!"
        elif result == "Win!":
            outcome_message = "You win!"
        else:
            outcome_message = "You lose!"

        print(f"You selected {user_item}. The computer selected {computer_item}. {outcome_message}")

        return result
    


