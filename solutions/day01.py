def part1(input):
    prev = None
    cnt = 0
    for idx, val in enumerate(input):
        if idx == 0:
            prev = val
            continue

        cnt += 1 if val > prev else 0
        prev = val
    return cnt

def part2(input):
    threes = []
    cnt = 0
    for idx, val in enumerate(input):
        if idx < 3:
            threes.append(val)
            continue

        prev_avg = sum(threes) / len(threes)
        threes.append(val)
        del threes[0]

        curr_avg = sum(threes) / len(threes)
        cnt += 1 if curr_avg > prev_avg else 0
    return cnt
