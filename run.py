from random import randint

board = []

for i in range(0, 5):
    board.append(["0"]*5)


def print_board(board):
    for i in board:
        print(" ".join(i))


print_board(board)


def random_row(board):
    return randint(0, len(board)-1)


def random_col(board):
    return randint(0, len(board)-1)


ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row: "))

guess_col = int(input("Guess Colum: "))


if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! Youve sunk my battleship")
else:
    print("Ha!Better luck next time, You missed my battleship.")
    board[guess_row][guess_col] = "x"
    print_board(board)