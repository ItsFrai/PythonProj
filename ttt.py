def playerinput():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
        
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
     
def display_board(board):
    print("-------------")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print("-------------")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("-------------")
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("-------------")
    
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    
def space_check(board, position):
    return board[position] == ' '

def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

        
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? (Y/N) ').lower().startswith('y')

#MAIN BELOW  - FUNCTIONS ABOVE

print('Welcome to Tic Tac Toe by Fraidoon Pourooshasb!')

while True:
    play_game = input('Are you ready to play? (Y/N) ').upper()
    if play_game == 'Y':
        game_on = True
    elif play_game == 'N':
        break
    else: 
        print("Incorrect Input")
        continue
    
    theBoard = [' '] * 10
    player1_marker, player2_marker = playerinput()
    turn = choose_first()
    print(turn + ' will go first.')
    

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    if replay() == False:
        break

            
        

    