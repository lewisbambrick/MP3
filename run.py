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


for turn in range(4):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))

    guess_col = int(input("Guess Colum: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You've sunk my battleship!")
        break
    else:
        if guess_row > 4 or guess_col > 4:
            print("Oops that wasn't even in the ocean!")
        elif board[guess_row][guess_col] == "x":
            print("You've already guessed there, select another target. ")
        else:
            print("Ha!Better luck next time, You missed my battleship.")
            board[guess_row][guess_col] = "x"
            if turn == 3:
                print("Game over, you're out of chances!")
            print_board(board)