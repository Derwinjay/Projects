# ------------GOAL--------------
# - | - | - | - | - | - | - 1
# ------------------------- 2
# - | - | - | - | - | - | - 3
# ------------------------- 4
# - | - | - | - | - | - | - 5
# ------------------------- 6
# - | - | - | - | - | - | - 7
# ------------------------- 8
# - | - | - | - | - | - | - 9
# ------------------------- 10
# - | - | - | - | - | - | - 11
# 1 2 3 4 5 6 7 8 9 0 1 2 3





CURRENT_BOARD = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
]


def draw_board(field):

    for row in range(11):
        newRow = int(row/2)
        if row % 2 == 0:
            for col in range(13):
                if col % 2 == 0:
                    newCol = int(col/2)
                    if col != 12:
                        # prints values from our list
                        print(field[newRow][newCol], end=" ")
                    else:
                        print(field[newRow][newCol])
                else:
                    print("|", end=" ")
        else:
            print("-------------------------")


def check_if_gameover():
    if check_col():
        print("It worked COLUMN WINNER!!!!\n")
        game = False
    elif check_row():
        print("It worked ROW WINNER!!\n")
        game = False
    elif check_Diagonal():
        print("It worked DIAGONAL WINNER!!!\n")
        game = False
    elif move_Counter == 42:
        print("NO CONTEST....The game is a tie.")
        game = False
    else:
       # print("It worked\n")
        game = True

    return game



def check_col():    #checks if winner is in a column
    for rows in range(3):
        for cols in range(7):
            if CURRENT_BOARD[rows][cols] == piece and CURRENT_BOARD[rows][cols] == CURRENT_BOARD[rows+1][cols] == CURRENT_BOARD[rows+2][cols] == CURRENT_BOARD[rows+3][cols]:
                print(piece, "Player is the WINNER!!!!")
                return True
    


def check_Diagonal():
    for rows in range(3):
        for cols in range(4): #checks the positive slope
            if CURRENT_BOARD[rows][cols] == piece and CURRENT_BOARD[rows][cols] == CURRENT_BOARD[rows+1][cols+1] == CURRENT_BOARD[rows+2][cols+2] == CURRENT_BOARD[rows+3][cols+3]:
                print(piece, "Player is the WINNER!!!!")
                return True #checks the negative slope
            if CURRENT_BOARD[rows][cols] == piece and CURRENT_BOARD[rows][cols] == CURRENT_BOARD[rows+1][cols-1] == CURRENT_BOARD[rows+2][cols-2] == CURRENT_BOARD[rows+3][cols-3]:
                print(piece, "Player is the WINNER!!!!")
                return True
    




def check_row():    #checks if winner is in a row
    for rows in range(6):
        for cols in range(4):
            if CURRENT_BOARD[rows][cols] == piece and CURRENT_BOARD[rows][cols] == CURRENT_BOARD[rows][cols + 1] == CURRENT_BOARD[rows][cols + 2] == CURRENT_BOARD[rows][cols + 3]:
                print(piece, "Player is the WINNER!!!!")
                return True
            



player = 1
game = True
draw_board(CURRENT_BOARD)  # Draws initial empty board
move_Counter = 0     #Keeps tract of number of turns and will end game if a certain amount of turns go by.
while(game):
    player_board_choice = int(
        input("Enter a column to place your piece. \n")) - 1

    # Decides whose turn it is
    if player_board_choice <= 6:
        if player == 1:
            piece = "O"
            print("It is", piece, "turn.")
            player = 2  # changes the player after code exicutes

        else:
            piece = "X"
            print("It is", piece, "turn.")
            player = 1

        if CURRENT_BOARD[-1][player_board_choice] == "-":  # Decides where a piece can go
            CURRENT_BOARD[-1][player_board_choice] = piece
        elif CURRENT_BOARD[-2][player_board_choice] == "-":
            CURRENT_BOARD[-2][player_board_choice] = piece
        elif CURRENT_BOARD[-3][player_board_choice] == "-":
            CURRENT_BOARD[-3][player_board_choice] = piece
        elif CURRENT_BOARD[-4][player_board_choice] == "-":
            CURRENT_BOARD[-4][player_board_choice] = piece
        elif CURRENT_BOARD[-5][player_board_choice] == "-":
            CURRENT_BOARD[-5][player_board_choice] = piece
        elif CURRENT_BOARD[-6][player_board_choice] == "-":
            CURRENT_BOARD[-6][player_board_choice] = piece
        else:
            print("This column is full. Pick anoother column.")

        # print(CURRENT_BOARD)
    else:
        print("The number you entered is too big. Please pick a column number 1-7")

    # draws the new updated board after a player has made a move
    draw_board(CURRENT_BOARD)
    move_Counter += 1
    print(move_Counter)
    game = check_if_gameover()
    if move_Counter == 42:
        print("Excessive amount of moves taken. Game is a draw.")
        game = False
