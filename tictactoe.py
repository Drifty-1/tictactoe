win = False
xTurn = True
oTurn = False

# starting board, to show user which number corresponds to where
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

# dictionary for board, to keep track of squares
board = {
    "square1" : ' ',
    "square2" : ' ',
    "square3" : ' ',
    "square4" : ' ',
    "square5" : ' ',
    "square6" : ' ',
    "square7" : ' ',
    "square8" : ' ',
    "square9" : ' ',
}

def printBoard(board):
    # function that prints out the current board
    print(f"{board['square1']} | {board['square2']} | {board['square3']}")
    print(f"{board['square4']} | {board['square5']} | {board['square6']}")
    print(f"{board['square7']} | {board['square8']} | {board['square9']}")

def getMoveX(board):
    # function that handles the move for Player X, and updates the board dictionary accordingly
    move = int(input("Player X, enter a number between 1 and 9 corresponding to the square you would like to move on: "))
    if move == 1 and board['square1'] == ' ': board['square1'] = 'X'
    elif move == 2 and board['square2'] == ' ': board['square2'] = 'X'
    elif move == 3 and board['square3'] == ' ': board['square3'] = 'X'
    elif move == 4 and board['square4'] == ' ': board['square4'] = 'X'
    elif move == 5 and board['square5'] == ' ': board['square5'] = 'X'
    elif move == 6 and board['square6'] == ' ': board['square6'] = 'X'
    elif move == 7 and board['square7'] == ' ': board['square7'] = 'X'
    elif move == 8 and board['square8'] == ' ': board['square8'] = 'X'
    elif move == 9 and board['square9'] == ' ': board['square9'] = 'X'

    global xTurn 
    xTurn = False
    global oTurn
    oTurn = True
    
    return board

def getMoveO(board):
    # function that handles the move for Player O, and updates the board dictionary accordingly
    move = int(input("Player O, enter a number between 1 and 9 corresponding to the square you would like to move on: "))
    if move == 1 and board['square1'] == ' ': board['square1'] = 'O'
    elif move == 2 and board['square2'] == ' ': board['square2'] = 'O'
    elif move == 3 and board['square3'] == ' ': board['square3'] = 'O'
    elif move == 4 and board['square4'] == ' ': board['square4'] = 'O'
    elif move == 5 and board['square5'] == ' ': board['square5'] = 'O'
    elif move == 6 and board['square6'] == ' ': board['square6'] = 'O'
    elif move == 7 and board['square7'] == ' ': board['square7'] = 'O'
    elif move == 8 and board['square8'] == ' ': board['square8'] = 'O'
    elif move == 9 and board['square9'] == ' ': board['square9'] = 'O'

    global xTurn 
    xTurn = True
    global oTurn
    oTurn = False
    
    return board

def checkWin(board):
    # function that checks for wins
    global win
    if win != True:
        # horizontal (left to right)
        if board['square1'] == board['square2'] == board['square3'] and board['square1'] != ' ':
            print(f"Player {board['square1']} has won.")
            win = True
        elif board['square4'] == board['square5'] == board['square6'] and board['square4'] != ' ':
            print(f"Player {board['square4']} has won.")
            win = True
        elif board['square7'] == board['square8'] == board['square9'] and board['square7'] != ' ':
            print(f"Player {board['square7']} has won.")
            win = True
        
        # vertical (up to down)
        elif board['square1'] == board['square4'] == board['square7'] and board['square1'] != ' ':
            print(f"Player {board['square1']} has won.")
            win = True
        elif board['square2'] == board['square5'] == board['square8'] and board['square2'] != ' ':
            print(f"Player {board['square2']} has won.")
            win = True
        elif board['square3'] == board['square6'] == board['square9'] and board['square4'] != ' ':
            print(f"Player {board['square4']} has won.")
            win = True
        
        # diagonal
        elif board['square1'] == board['square5'] == board['square9'] and board['square1'] != ' ':
            print(f"Player {board['square1']} has won.")
            win = True
        elif board['square3'] == board['square5'] == board['square7'] and board['square3'] != ' ':
            print(f"Player {board['square3']} has won.")
            win = True

    # check for ties
        elif board['square1'] != ' ' and board['square2'] != ' ' and board['square3'] != ' ' and board['square4'] != ' ' and board['square5'] != ' ' and board['square6'] != ' ' and board['square7'] != ' ' and board['square8'] != ' ' and board['square9'] != ' ':
            print("The game has ended in a tie.")
    
    return


while win != True:
    if xTurn == True:
        getMoveX(board)
    elif oTurn == True:
        getMoveO(board)
    printBoard(board)
    checkWin(board)