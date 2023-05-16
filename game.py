from board import Board
import time
import random
import math
from minimax import minimax
# import alphabeta
# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES

        # YOUR CODE GOES HERE
        (colum, value) = minimax(game_board, 3, -math.inf, math.inf, True)
        print("Column HERE 000000000000000000")
        print(colum)
        print(game_board)
        board.print_grid(game_board)
        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        # random_column = random.randint(0, 6)
        board.select_column(colum)

        time.sleep(2)


if __name__ == "__main__":
    main()
