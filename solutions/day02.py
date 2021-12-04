def part1(input):
    position = 0
    depth = 0
    for command in input:
        direction, value = command.rstrip().split(' ')
        if direction == 'forward':
            position = position + int(value)
        if direction == 'down':
            depth = depth + int(value)
        if direction == 'up':
            depth = depth - int(value)
    return position * depth

def part2(input):
    position = 0
    depth = 0
    aim = 0
    for command in input:
        direction, value = command.rstrip().split(' ')
        if direction == 'forward':
            position = position + int(value)
            depth = depth + aim * int(value)
        if direction == 'down':
            aim = aim + int(value)
        if direction == 'up':
            aim = aim - int(value)
    return position * depth
