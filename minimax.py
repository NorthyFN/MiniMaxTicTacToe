def check_board_status(fields_pos, grid_size, winning_length):
    # check horizontal
    for y in range(grid_size):
        in_a_row_horizontal = 0
        last_player = " "
        for x in range(grid_size):
            if fields_pos[y][x] != last_player and fields_pos[y][x] != " ":
                in_a_row_horizontal = 1
                last_player = fields_pos[y][x]
            elif fields_pos[y][x] == last_player and fields_pos[y][x] != " ":
                in_a_row_horizontal += 1
            else:
                in_a_row_horizontal = 0
                last_player = " "
            if in_a_row_horizontal == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    # check vertical
    for x in range(grid_size):
        in_a_row_vertical = 0
        last_player = " "
        for y in range(grid_size):
            if fields_pos[y][x] != last_player and fields_pos[y][x] != " ":
                in_a_row_vertical = 1
                last_player = fields_pos[y][x]
            elif fields_pos[y][x] == last_player and fields_pos[y][x] != " ":
                in_a_row_vertical += 1
            else:
                in_a_row_vertical = 0
                last_player = " "
            if in_a_row_vertical == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    # check diagonal-right
    for x in range(grid_size):
        in_a_row_diagonal_right = 0
        last_player = " "
        for y in range(grid_size - x):
            if fields_pos[y][x+y] != last_player and fields_pos[y][x+y] != " ":
                in_a_row_diagonal_right = 1
                last_player = fields_pos[y][x+y]
            elif fields_pos[y][x+y] == last_player and fields_pos[y][x+y] != " ":
                in_a_row_diagonal_right += 1
            else:
                in_a_row_diagonal_right = 0
                last_player = " "
            if in_a_row_diagonal_right == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    for y in range(1, grid_size):
        in_a_row_diagonal_right = 0
        last_player = " "
        for x in range(grid_size - y):
            if fields_pos[y+x][x] != last_player and fields_pos[y+x][x] != " ":
                in_a_row_diagonal_right = 1
                last_player = fields_pos[y+x][x]
            elif fields_pos[y+x][x] == last_player and fields_pos[y+x][x] != " ":
                in_a_row_diagonal_right += 1
            else:
                in_a_row_diagonal_right = 0
                last_player = " "
            if in_a_row_diagonal_right == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    # check diagonal-left
    for x in range(grid_size):
        in_a_row_diagonal_left = 0
        last_player = " "
        for y in range(x+1):
            if fields_pos[y][x-y] != last_player and fields_pos[y][x-y] != " ":
                in_a_row_diagonal_left = 1
                last_player = fields_pos[y][x-y]
            elif fields_pos[y][x-y] == last_player and fields_pos[y][x-y] != " ":
                in_a_row_diagonal_left += 1
            else:
                in_a_row_diagonal_left = 0
                last_player = " "
            if in_a_row_diagonal_left == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    for y in range(1, grid_size):
        in_a_row_diagonal_left = 0
        last_player = " "
        # print(f"Y: {y}  Range X: {grid_size - y}" )  # Debug
        for x in range(grid_size - y):
            # print(f"Scanning coordinates y:{y+x} x:{-x-1}")  # Debug
            if fields_pos[y+x][-x-1] != last_player and fields_pos[y+x][-x-1] != " ":
                in_a_row_diagonal_left = 1
                last_player = fields_pos[y+x][-x-1]
            elif fields_pos[y+x][-x-1] == last_player and fields_pos[y+x][-x-1] != " ":
                in_a_row_diagonal_left += 1
            else:
                in_a_row_diagonal_left = 0
                last_player = " "
            if in_a_row_diagonal_left == winning_length:
                if last_player == "X":
                    return 1
                elif last_player == "0":
                    return -1

    for y in range(grid_size):
        for x in range(grid_size):
            if fields_pos[y][x] == " ":
                return None

    return 0


def get_available_positions(field_pos):
    available = []
    for y in range(len(field_pos)):
        for x in range(len(field_pos)):
            if field_pos[y][x] == " ":
                available.append([y, x])
    return available


def minimax(position, depth, alpha, beta, maximizingPlayer, grid_size, winning_length):
    depth_count = 0
    result = check_board_status(position, grid_size, winning_length)
    if depth == 0:
        return 0, depth_count + 1
    elif result is not None:
        return result, depth_count + 1

    if maximizingPlayer:
        maxEval = -float("inf")  # maxEval is set to negative Infinity
        brk = False
        for y in range(len(position)):
            if brk:
                break
            for x in range(len(position)):
                if position[y][x] == " ":
                    position[y][x] = "X"
                    temp_eval, recovered_depth = minimax(position, depth - 1, alpha, beta, False, grid_size, winning_length)
                    position[y][x] = " "
                    maxEval = max(maxEval, temp_eval)
                    depth_count += recovered_depth

                    # Alpha Beta Pruning
                    alpha = max(alpha, temp_eval)
                    if beta <= alpha:
                        brk = True
                        break
        # print("MIN-EVAL at MAX at return:", maxEval, "At depth:", depth)  # debug
        return maxEval, depth_count

    else:
        minEval = float("inf")  # minEval is set to Infinity
        brk = False
        for y in range(len(position)):
            if brk:
                break
            for x in range(len(position)):
                if position[y][x] == " ":
                    position[y][x] = "0"
                    temp_eval, recovered_depth = minimax(position, depth - 1, alpha, beta, True, grid_size, winning_length)
                    position[y][x] = " "
                    minEval = min(minEval, temp_eval)
                    depth_count += recovered_depth

                    # Alpha Beta Pruning
                    beta = min(beta, temp_eval)
                    if beta <= alpha:
                        brk = True
                        break
        # print("MIN-EVAL at MINI at return:",minEval,"At depth:",depth)  # debug
        return minEval, depth_count
