# TIC TAC TOE GAME
#GLOBAL VARIABLES
board = ['-','-','-',
         '-','-','-',
         '-','-','-',]

game_goes_on = True
winner = None

# def display_board():
#     # print(board[0]+'|'+board[1]+'|'+board[2])
#     # print(board[3]+'|'+board[4]+'|'+board[5])
#     # print(board[6]+'|'+board[7]+'|'+board[8])
#     # OOOOOOORRRRR
#     print("***********")
#     print('*  ' + board[0]+'|'+board[1]+'|'+board[2] + '  *')
#     print('*  ' + board[3]+'|'+board[4]+'|'+board[5] + '  *')
#     print('*  ' + board[6]+'|'+board[7]+'|'+board[8] + '  *')
#     print("***********")

#OOOOOOORRRRR ----------------------------------
# print(list(range(0, 9, 3)))
def display_board():
    print("***********")
    for i in range(0, 9, 3):
        print('*  ' + board[i] + '|' + board[i+1] + '|' + board[i+2] + '  *')
    print("***********")


# starting the game

def player_input(current_player):
    valid = False
    while not valid:
        position = int(input(f'{current_player} choose a position from 1 to 9:'))-1
        if 0 <= position < 9 and board[position] == '-':
            board[position] = current_player
            valid = True
        else:
            print('Invalid position. Choose a number between 1 and 9.')

def check_winner():
    global winner
    global game_goes_on    
    # check rows
    # if board[0] == board[1] == board[2] != "-":
    #     game_goes_on = False
    #     winner = board[0]
    #     return winner
    # elif board[3] == board[4] == board[5] != "-":
    #     game_goes_on = False
    #     winner = board[3]
    #     return winner
    # elif board[6] == board[7] == board[8] != "-":
    #     game_goes_on = False
    #     winner = board[6]
    #     return winner
    
    # # check columns   
    # if board[0] == board[3] == board[6] != "-":
    #     winner = board[0]
    #     game_goes_on = False
    #     return winner
    # if board[1] == board[4] == board[7] != "-":
    #     winner = board[1]
    #     game_goes_on = False
    #     return winner
    # if board[2] == board[5] == board[8] != "-":
    #     winner = board[2]
    #     game_goes_on = False
    #     return winner
    
    # # check diagonals
    # if board[0] == board[4] == board[8] != "-":
    #     game_goes_on = False
    #     winner = board[0]
    #     return winner
    # elif board[2] == board[4] == board[6] != "-":
    #     game_goes_on = False
    #     winner = board[2]
    #     return winner
    
    # OOOOOR USING COORDINATES TUPLES:
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for coord in win_coord:
        if board[coord[0]] == board[coord[1]] == board[coord[2]] != "-":
            winner = board[coord[0]]
            game_goes_on = False
            return winner

    # check tie
    if '-' not in board and winner == None:
        winner = 'Tie'
        game_goes_on = False
        return winner
    
def play_game():
    while game_goes_on:
        display_board()
        players = ['X','O']
        for current_player in players:
            player_input(current_player)
            display_board()
            winner = check_winner()
            if winner == 'Tie':
                return print('Tie')
            elif winner != None:
                return print(f'{winner} won the game')
            
play_game()
        
       


