#Rock Paper Scissors Exercise

import random

class Game:
    """
    Represents a game of Rock, Paper, Scissors.
    """
    
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        """
        Asks the user to select an item and validates the input.
        """
        while True:
            user_input = input("Select an item (rock, paper, or scissors): ").lower()
            if user_input in self.items:
                return user_input
            print("Invalid selection. Please choose from rock, paper, or scissors.")

    def get_computer_item(self):
        """
        Randomly selects an item for the computer.
        """
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """
        Determines the result of the game based on the items.
        """
        if user_item == computer_item:
            return 'draw'
        
        # Win conditions for the user
        if (user_item == 'rock' and computer_item == 'scissors') or \
           (user_item == 'paper' and computer_item == 'rock') or \
           (user_item == 'scissors' and computer_item == 'paper'):
            return 'win'
        
        # All other cases are a loss
        return 'loss'

    def play(self):
        """
        Plays a single game of Rock, Paper, Scissors.
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        print(f"\nYou selected {user_item}. The computer selected {computer_item}. You {result}!")
        return result

def get_user_menu_choice():
    """
    Displays the menu and gets the user's choice.
    """
    print("\nMenu:")
    print("(p) Play a new game")
    print("(s) Show scores")
    print("(q) Quit")
    
    user_choice = input("Enter your choice: ").lower().strip()
    return user_choice

def print_results(results):
    """
    Prints the final game results in a user-friendly way.
    """
    print("\n*** GAME SCORES ***")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("\nThank you for playing!")

def main():
    """
    The main function to run the Rock, Paper, Scissors game.
    """
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice == 'p':
            game = Game()
            game_result = game.play()
            
            # Update the results dictionary with the new game's outcome
            if game_result in results:
                results[game_result] += 1

        elif user_choice == 's':
            print_results(results)

        elif user_choice == 'q':
            print_results(results)
            break
            
        else:
            print("Invalid choice. Please select 'p', 's', or 'q'.")

if __name__ == "__main__":
    main()