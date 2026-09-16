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
    
#Other Data for game listed below

#Rock-Paper-Scissors - This contains the functions to show the main menu, handle user input, and show game summary when exiting.

from game import Game

def get_user_menu_choice():
    """Displays the menu and gets the user's choice without looping."""
    print("\n--- Rock, Paper, Scissors Menu ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit (or type 'q' / 'x')")

    choice = input("Enter your choice: ").strip().lower()

    #Simple data validation without looping (handled in main)
    if choice in ['1', '2', '3', 'q', 'x']:
        return choice
    else:
        print("Invalid menu choice. Please try again.")
        return None
    
def print_results(results):
    """Displays a summary of all games played."""
    print("\n---Game Summary---")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("\nThank you for playing!")

def main():
    #Initialize the results dictionary to keep track of scores
    results = {'win': 0, 'loss': 0, 'draw': 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            #Create a new game object and play
            current_game = Game()
            game_result = current_game.play()

            #Update the results dictionary using the returned string
            results[game_result] += 1

        elif choice == '2':
            #Display current scores without quitting
            print(f"\nCurrent Scores -> Wins: {results['win']} | Losses: {results['loss']} | Draws: {results['draw']}")

        elif choice in ['3', 'q', 'x']:
            #Call print_results to show the final summary and break the loop
            print_results(results)
            break

if __name__ == "__main__":
    main()

