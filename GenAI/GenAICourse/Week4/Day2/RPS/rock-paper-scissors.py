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