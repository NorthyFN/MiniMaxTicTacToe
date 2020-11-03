import string
import numpy as np
import minimax as mm
# import os
# import random


def draw_grid(grid_size,fields):
    for y in range(grid_size):
        for x in range(grid_size):
            print("|" + fields[y][x], end="")
        print("|", y + 1)


def draw_column_letters(letters):
    for i in range(len(letters)):
        print(f" {letters[i]}", end="")
        if i + 1 == len(letters):
            print("")


def make_move(fields, is_player, print_score=False):
    if is_player:
        move_ok = False
        while not move_ok:
            move = input("Make a move: ")
            column = string.ascii_lowercase.index(move[0].lower())
            row = int(move[1]) - 1
            if fields[row][column] != " ":
                print("The chosen field is unavailable...")
            else:
                fields[row][column] = "X"
                return fields
    elif not is_player:
        """while True:  # pick random
            column = random.randint(0,GRID_SIZE-1)
            row = random.randint(0,GRID_SIZE-1)
            if fields[row][column] == " ":
                break
        fields[row][column] = "0"""""
        possible_paths = 0
        move = []
        minEval = float("inf")
        for y in range(len(fields)):
            for x in range(len(fields)):
                if fields[y][x] == " ":
                    fields[y][x] = "0"
                    temp_eval, recovered_depth = mm.minimax(fields, MINIMAX_DEPTH, -INFINITY, INFINITY, True, GRID_SIZE, WINNING_LENGTH)
                    fields[y][x] = " "
                    if temp_eval < minEval:
                        minEval = temp_eval
                        move = [y,x]
                    possible_paths += recovered_depth

                    if print_score:
                        print(f"\nField {column_letters[x]}{y + 1} score: {temp_eval}", end="")

        fields[move[0]][move[1]] = "0"

        print(f"\nChecked {possible_paths} possible paths.")
        return fields


def check_board_status(fields, grid_size, winning_length):
    full = True

    # check horizontal
    for y in range(grid_size):
        in_a_row_horizontal = 0
        last_player = " "
        for x in range(grid_size):
            if fields[y][x] != last_player and fields[y][x] != " ":
                in_a_row_horizontal = 1
                last_player = fields[y][x]
            elif fields[y][x] == last_player and fields[y][x] != " ":
                in_a_row_horizontal += 1
            else:
                in_a_row_horizontal = 0
                last_player = " "
            if in_a_row_horizontal == winning_length:
                print(f"\n{last_player} won!")
                return True

    # check vertical
    for x in range(grid_size):
        in_a_row_vertical = 0
        last_player = " "
        for y in range(grid_size):
            if fields[y][x] != last_player and fields[y][x] != " ":
                in_a_row_vertical = 1
                last_player = fields[y][x]
            elif fields[y][x] == last_player and fields[y][x] != " ":
                in_a_row_vertical += 1
            else:
                in_a_row_vertical = 0
                last_player = " "
            if in_a_row_vertical == winning_length:
                print(f"\n{last_player} won!")
                return True

    # check diagonal-right
    for x in range(grid_size):
        in_a_row_diagonal_right = 0
        last_player = " "
        for y in range(grid_size - x):
            if fields[y][x+y] != last_player and fields[y][x+y] != " ":
                in_a_row_diagonal_right = 1
                last_player = fields[y][x+y]
            elif fields[y][x+y] == last_player and fields[y][x+y] != " ":
                in_a_row_diagonal_right += 1
            else:
                in_a_row_diagonal_right = 0
                last_player = " "
            if in_a_row_diagonal_right == winning_length:
                print(f"\n{last_player} won!")
                return True

    for y in range(1, grid_size):
        in_a_row_diagonal_right = 0
        last_player = " "
        for x in range(grid_size - y):
            if fields[y+x][x] != last_player and fields[y+x][x] != " ":
                in_a_row_diagonal_right = 1
                last_player = fields[y+x][x]
            elif fields[y+x][x] == last_player and fields[y+x][x] != " ":
                in_a_row_diagonal_right += 1
            else:
                in_a_row_diagonal_right = 0
                last_player = " "
            if in_a_row_diagonal_right == winning_length:
                print(f"\n{last_player} won!")
                return True

    # check diagonal-left
    for x in range(grid_size):
        in_a_row_diagonal_left = 0
        last_player = " "
        for y in range(x+1):
            if fields[y][x-y] != last_player and fields[y][x-y] != " ":
                in_a_row_diagonal_left = 1
                last_player = fields[y][x-y]
            elif fields[y][x-y] == last_player and fields[y][x-y] != " ":
                in_a_row_diagonal_left += 1
            else:
                in_a_row_diagonal_left = 0
                last_player = " "
            if in_a_row_diagonal_left == winning_length:
                print(f"\n{last_player} won!")
                return True

    for y in range(1, grid_size):
        in_a_row_diagonal_left = 0
        last_player = " "
        # print(f"Y: {y}  Range X: {grid_size - y}" )  # Debug
        for x in range(grid_size - y):
            # print(f"Scanning coordinates y:{y+x} x:{-x-1}")  # Debug
            if fields[y+x][-x-1] != last_player and fields[y+x][-x-1] != " ":
                in_a_row_diagonal_left = 1
                last_player = fields[y+x][-x-1]
            elif fields[y+x][-x-1] == last_player and fields[y+x][-x-1] != " ":
                in_a_row_diagonal_left += 1
            else:
                in_a_row_diagonal_left = 0
                last_player = " "
            if in_a_row_diagonal_left == winning_length:
                print(f"\n{last_player} won!")
                return True

    # check if board is full
    for i in range(grid_size):
        for j in range(grid_size):
            if fields[i][j] == " ":
                full = False

    # return
    if full:
        print("\nTie!")
        return True
    else:
        return False


INFINITY = float("inf")
# ---------------------------
MINIMAX_DEPTH = 9
GRID_SIZE = 3
WINNING_LENGTH = 3
AI_FIRST = True
PRINT_FIELD_SCORE = False
# ---------------------------

field_list = np.array([[" ", ] * GRID_SIZE] * GRID_SIZE)

alphabet_list = list(string.ascii_uppercase)
column_letters = alphabet_list[:GRID_SIZE]


finished = False
if AI_FIRST:
    # ai
    draw_column_letters(column_letters)
    draw_grid(GRID_SIZE, field_list)
    if check_board_status(field_list, GRID_SIZE, WINNING_LENGTH):
        finished = True
    temp_list = make_move(field_list, False, True if PRINT_FIELD_SCORE else False)
    field_list = temp_list

while not finished:

    # human
    draw_column_letters(column_letters)
    draw_grid(GRID_SIZE, field_list)
    if check_board_status(field_list, GRID_SIZE, WINNING_LENGTH):
        break
    field_list = make_move(field_list, True)
    # os.system('cls')

    # ai
    draw_column_letters(column_letters)
    draw_grid(GRID_SIZE, field_list)
    if check_board_status(field_list, GRID_SIZE, WINNING_LENGTH):
        break
    temp_list = make_move(field_list, False, True if PRINT_FIELD_SCORE else False)
    field_list = temp_list
    # os.system('cls')

