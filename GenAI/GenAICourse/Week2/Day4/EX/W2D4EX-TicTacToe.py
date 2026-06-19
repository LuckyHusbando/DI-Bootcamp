#W2D4EX

#Mini-Project - Tic-Tac-Toe

#Parameters:

# Create A List of Lists to represent the game board. Each cell should be represented by " "
# display_board() - represent current state of board
# player_input(player) - how to ask, how to validate
# check_win(board, player) - has current player won?
# If won, return True; otherwise, return False.
# How to Check every winning combination?
# How to check for a Tie? Check all positions for entry.
# Play() manages game flow.
# Initialize game board
# While loop to continue game until winner or tie.
# Inside loop: Display, Get current player input, update board, check for winner, check for tie, switch to next player.
# Helper functions to break down logic to smaller parts.
# Single responsibility function - each function does one thing and does it well.
# How to swap players, how to store player symbols?

def create_board():
    #Creates a 3x3 list of lists filled with spaces.
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def display_board(board):
    #Iterates through each row and prints with vertical and horizontal dividers.
    for i in range(3):
        print(" " + "  |  ".join(board[i]))
        if i < 2:
            print("-----" * 3)

def player_input(board, player):
    #Choose which player's turn it is.
    print(f"\nPlayer {player}'s turn. (Type 'q' to quit)")
    while True:
        try:
            #Take the input as text first.
            row_raw = input("Enter row (0, 1, or 2): ").strip().lower()
            if row_raw == 'q' or row_raw == 'quit':
                return "quit"
            
            col_raw = input("Enter column (0, 1, or 2): ").strip().lower()
            if col_raw == 'q' or col_raw == 'quit':
                return "quit"
            
            #If they did not quit, convert to integers.
            row = int(row_raw)
            col = int(col_raw)
                
            #Check if coordinates are within the board limits.
            if row in [0, 1, 2] and col in [0, 1, 2]:
                #Check if spot is taken
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken. Try again!")
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter actual numbers.")

def check_win(board, player): #Check for win-state
    #Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
        
    #Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
        
    #Check diagonals
    if board[0][0] == [board[1][1]] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def check_tie(board): #Check for tie-state
    for row in board:
        if " " in row:
            return False #Found an empty space, so it is not a tie yet.
    return True #No empty spaces found.

def play(): #The brain of the game.
    #Initialize game board.
    board = create_board()
    current_player = "X"
    game_on = True

    print("Welcome to Derek's Tic-Tac-Toe!")
    display_board(board)

    #While loop to continue game until winner or tie
    while game_on:
        #Capture the movie in one variable first
        move = player_input(board, current_player)

        #Check for quit signal
        if move == "quit":
            print("\nGame cancelled! Thanks for playing!")
            break

        #Now safe to unpack two variables
        row, col = move

        #Update board
        board[row][col] = current_player

        #Display updated board
        display_board(board)

        #Check game state
        if check_win(board, current_player):
            print(f"\n Congraulations! Player {current_player} wins!")
            game_on = False
        elif check_tie(board):
            print("\nIt's a tie game! Wow!")
            game_on = False
        else:
            current_player = "O" if current_player == "X" else "X"

#Game trigger to start when script run
if __name__ == "__main__":
    play()

#-------------

