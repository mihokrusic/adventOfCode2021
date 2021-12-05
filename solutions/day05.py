def part1(input):
    parsed_input = [x.rstrip().split(' -> ') for x in input]
    board = dict()

    for line in parsed_input:
        line_from = [int(x) for x in line[0].split(',')]
        line_to = [int(x) for x in line[1].split(',')]

        is_diagonal = line_from[0] != line_to[0] and line_from[1] != line_to[1]
        if not is_diagonal:
            __fill_straight(board, line_from, line_to)

    return __get_crosses(board)

def part2(input):
    parsed_input = [x.rstrip().split(' -> ') for x in input]
    board = dict()

    for line in parsed_input:
        line_from = [int(x) for x in line[0].split(',')]
        line_to = [int(x) for x in line[1].split(',')]

        is_diagonal = line_from[0] != line_to[0] and line_from[1] != line_to[1]
        if not is_diagonal:
            __fill_straight(board, line_from, line_to)
        else:
            __fill_diagonal(board, line_from, line_to)

    return __get_crosses(board)

def __fill_straight(board, line_from, line_to):
    from_x = min(line_from[0], line_to[0])
    to_x = max(line_from[0], line_to[0])
    from_y = min(line_from[1], line_to[1])
    to_y = max(line_from[1], line_to[1])
    for x in range(from_x, to_x + 1):
        for y in range(from_y, to_y + 1):
            __add_to_board([x, y], board)

def __fill_diagonal(board, line_from, line_to):
    min_x = min(line_from[0], line_to[0])
    max_x = max(line_from[0], line_to[0])

    current = line_from.copy()
    delta_x = 1 if line_to[0] > line_from[0] else -1
    delta_y = 1 if line_to[1] > line_from[1] else -1
    for _ in range(max_x - min_x + 1):
        __add_to_board(current, board)
        current[0] += delta_x
        current[1] += delta_y

def __add_to_board(pos, board):
    key = str(pos[0]) + "-" + str(pos[1])
    board[key] = 1 if key not in board else board[key] + 1

def __get_crosses(board):
    crosses = 0
    for key in board.keys():
        if board[key] > 1:
            crosses += 1
    return crosses