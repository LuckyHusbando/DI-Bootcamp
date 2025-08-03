#Mini Project - Tic-Tac-Toe

import sys #Used for sys.exit() to stop the program if needed.

# --- Step 1: Representing the Game Board ---
# The board is a 3x3 grid, initialized with spaces
board = [[' ' for _ in range(3)] for _ in range(3)]

# --- Step 2: Displaying the Game Board ---
def display_board(current_board):
    """
    Prints the current state of the Tic-Tac-Toe game board.
    """
    print("\n    0   1   2")
    print("----------------")
    for i, row in enumerate(current_board):
        print(f"{i} | {' | '.join(row)} |")
        print("----------------")
    print() # Add an extra newline for better spacing

# --- Step 3: Getting Player Input ---
def player_input(current_board, player_symbol):
    """
    Gets valid input from the current player for their move.
    Ensures input is within range and the cell is empty.
    Returns the chosen row and column as a tuple (row, col).
    """
    while True:
        try:
            row = int(input(f"Player {player_symbol}, enter your row (0, 1, or 2): "))
            col = int(input(f"Player {player_symbol}, enter your column (0, 1, or 2): "))

            # Validate input range
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid row or column. Please enter numbers between 0 and 2.")
                continue

            # Validate if the cell is empty
            if current_board[row][col] != ' ':
                print("That cell is already taken! Please choose an empty cell.")
                continue

            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers for row and column.")

# --- Step 4: Checking for a Winner ---
def check_win(current_board, player_symbol):
    """
    Checks if the current player has won the game.
    Returns True if the player has won, False otherwise.
    """
    # Check rows
    for row in current_board:
        if all(cell == player_symbol for cell in row):
            return True

    # Check columns
    for col_idx in range(3):
        if all(current_board[row_idx][col_idx] == player_symbol for row_idx in range(3)):
            return True

    # Check diagonals
    # Main diagonal (top-left to bottom-right)
    if all(current_board[i][i] == player_symbol for i in range(3)):
        return True
    # Anti-diagonal (top-right to bottom-left)
    if all(current_board[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False

# --- Step 5: Checking for a Tie ---
def check_tie(current_board):
    """
    Checks if the game has resulted in a tie (board is full and no winner).
    Returns True if it's a tie, False otherwise.
    """
    for row in current_board:
        if ' ' in row: # If any cell is still empty, it's not a tie yet
            return False
    return True # All cells are filled, and no winner (checked in main loop)

# --- Step 6: The Main Game Loop ---
def play_tic_tac_toe():
    """
    Manages the overall flow of the Tic-Tac-Toe game.
    """
    global board # Use the global board defined outside the function
    board = [[' ' for _ in range(3)] for _ in range(3)] # Reset board for new game

    players = ['X', 'O']
    current_player_idx = 0 # Start with 'X'

    print("Welcome to Tic-Tac-Toe!")

    while True:
        player_symbol = players[current_player_idx]
        
        display_board(board)
        print(f"It's Player {player_symbol}'s turn.")

        row, col = player_input(board, player_symbol)
        board[row][col] = player_symbol # Update the board with the player's move

        # Check for a winner
        if check_win(board, player_symbol):
            display_board(board)
            print(f"Congratulations, Player {player_symbol}! You win!")
            break # End the game loop

        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie! No one wins.")
            break # End the game loop

        # Switch to the next player
        current_player_idx = (current_player_idx + 1) % 2 # This elegantly switches between 0 and 1

    print("\nGame Over!")
    
    # Offer to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            play_tic_tac_toe() # Start a new game
            return # Exit the current function call to avoid multiple nested games
        elif play_again == 'no':
            print("Thanks for playing!")
            sys.exit() # Exit the program
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Start the game!
if __name__ == "__main__":
    play_tic_tac_toe()