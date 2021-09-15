from random import randint

board = []

for i in range(0, 5):
    board.append(["0"]*5)


def print_board(board):
    for i in board:
        print(" ".join(i))


def random_row(board):
    return randint(0, len(board)-1)


def random_col(board):
    return randint(0, len(board)-1)