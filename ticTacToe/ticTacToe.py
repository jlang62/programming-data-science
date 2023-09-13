# import numpy and random
import numpy as np
import random

# needed functions:
# create_board() - creates a 3x3 matrix of zeros
# random_place(board, player) - randomly places a player (1 or 2) on the board
# play_game() - creates a board, calls random_place(board, player) to place the players alternatively on the board,
# row_win(), col_win(), and diag_win() to check if the players have won after every placement.


def create_board():
    # Create a 3x3 matrix of zeros
    return np.zeros((3, 3))


def random_place(board, player):
    # randomly places a player (X or O) on the board
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    board[row][col] = player


def row_win(board, player):
    # check if any row has all the elements equal to player
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    return False


def col_win(board, player):
    # check if any column has all the elements equal to player
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False


def diag_win(board, player):
    # check if any diagonal has all the elements equal to player
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False


def play_game():
    board = create_board()
    print(board)

    # alternate between players
    for i in range(9):
        if i % 2 == 0:
            player = 1
        else:
            player = 2
        random_place(board, player)
        print(board)
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            print("Player " + str(player) + " wins after " + str(i+1) + " moves.")
            break


play_game()
