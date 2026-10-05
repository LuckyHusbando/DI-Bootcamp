#Mini Project - Tic-Tac-Toe Version 2

# The Tic Tac Toe game board represented as a list
# Each index corresponds to a square, 0-8
board = [" " for _ in range(9)]

def display_board():
    """
    Displays the current state of the Tic Tac Toe board.
    """
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}     1 | 2 | 3")
    print("---------     ---------")
    print(f"{board[3]} | {board[4]} | {board[5]}     4 | 5 | 6")
    print("---------     ---------")
    print(f"{board[6]} | {board[7]} | {board[8]}     7 | 8 | 9")
    print("\n")

def player_input(player):
    """
    Gets a valid position from the player and updates the board.
    """
    while True:
        try:
            position = int(input(f"Player {player}, choose a position (1-9): "))
            # Check if the position is within the valid range
            if 1 <= position <= 9:
                # Check if the chosen square is empty
                if board[position - 1] == " ":
                    board[position - 1] = player
                    break
                else:
                    print("This square is already taken. Please choose an empty one.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win():
    """
    Checks all winning conditions (rows, columns, diagonals) and for a tie.
    Returns the winner ('X' or 'O'), 'tie', or 'continue'.
    """
    # Helper function to check a list of three squares
    def check_line(line):
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]
        return None

    # Check rows
    for i in range(0, 9, 3):
        winner = check_line(board[i:i+3])
        if winner:
            return winner

    # Check columns
    for i in range(3):
        winner = check_line([board[i], board[i+3], board[i+6]])
        if winner:
            return winner
    
    # Check diagonals
    winner = check_line([board[0], board[4], board[8]])
    if winner:
        return winner
        
    winner = check_line([board[2], board[4], board[6]])
    if winner:
        return winner

    # Check for a tie (if all squares are full)
    if " " not in board:
        return "tie"

    # If no win or tie, the game continues
    return "continue"

def play():
    """
    The main function to run the Tic Tac Toe game.
    """
    current_player = 'X'
    game_result = "continue"

    print("Welcome to Tic Tac Toe!")
    display_board()

    while game_result == "continue":
        # Handle a single turn for the current player
        player_input(current_player)
        
        # Display the updated board
        display_board()
        
        # Check if the game has ended
        game_result = check_win()
        
        if game_result == "continue":
            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

    # Game has ended, print the final result
    if game_result == 'tie':
        print("The game is a tie!")
    else:
        print(f"Congratulations! Player {game_result} wins!")

# Start the game
if __name__ == "__main__":
    play()

#end