def part1(input):
    numbers_drawn  = [int(x) for x  in input[0].split(",")]
    boards = __get_boards(input)

    for number in numbers_drawn:
        __mark_boards(boards, number)
        winning = __find_winners(boards)
        if len(winning) > 0:
            winning_board = boards[winning[0]]
            return __get_sum_unmarked_items(winning_board) * number

    return None

def part2(input):
    numbers_drawn  = [int(x) for x  in input[0].split(",")]
    boards = __get_boards(input)

    winning_boards = []

    for number in numbers_drawn:
        __mark_boards(boards, number)
        winning = __find_winners(boards)
        if len(winning) > 0:
            for winning_idx in winning:
                if boards[winning_idx] not in winning_boards:
                    winning_boards.append(boards[winning_idx])

            if len(winning_boards) == len(boards):
                last_winner_board = winning_boards[-1]
                return __get_sum_unmarked_items(last_winner_board) * number

    return None

def __get_boards(input):
    boards = []
    current_board = []

    for line in input[2:]:
        if len(line.rstrip()) == 0:
            boards.append(current_board)
            current_board = []
            continue

        row = [(int(x), False) for x in list(filter(len, line.rstrip().split(" ")))]
        current_board.append(row)

    boards.append(current_board)
    return boards

def __mark_boards(boards, number):
    for board in boards:
        for row in board:
            for idx, item in enumerate(row):
                if item[0] == number:
                    row[idx] = (number, True)

def __find_winners(boards):
    winners = []
    for idx, board in enumerate(boards):
        for r in range(len(board)):
            row_filled = True
            col_filled = True
            for c in range(len(board)):
                if board[r][c][1] == False:
                    row_filled = False
                if board[c][r][1] == False:
                    col_filled = False

            if row_filled == True or col_filled == True:
                winners.append(idx)

    return winners

def __get_sum_unmarked_items(board):
    unmarked_sum = 0
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c][1] == False:
                unmarked_sum += board[r][c][0]
    return unmarked_sum
