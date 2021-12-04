def part1(input):
    commands = [[int(x) for x in list(line.rstrip())] for line in input]

    counter = __get_counter(commands)

    gamma = ''.join(['1' if x > len(input) / 2 else '0' for x in counter])
    epsilon = ''.join(['1' if x < len(input) / 2 else '0' for x in counter])
    return int(gamma, 2) * int(epsilon, 2)

def part2(input):
    oxygen_commands = [[int(x) for x in list(line.rstrip())] for line in input]
    scrubber_commands = oxygen_commands.copy()

    oxygen_rating = None
    scrubber_rating = None
    digit = 0

    while oxygen_rating == None or scrubber_rating == None:
        if oxygen_rating == None:
            counter_oxygen = __get_counter(oxygen_commands)
            oxygen_digit = 1 if counter_oxygen[digit] >= len(oxygen_commands) / 2 else 0
            oxygen_commands = list(filter(lambda i: i[digit] == oxygen_digit, oxygen_commands))

            if len(oxygen_commands) == 1:
                oxygen_rating = oxygen_commands[0]

        if scrubber_rating == None:
            counter_scrubber = __get_counter(scrubber_commands)
            scrubber_digit = 0 if counter_scrubber[digit] >= len(scrubber_commands) / 2 else 1
            scrubber_commands = list(filter(lambda i: i[digit] == scrubber_digit, scrubber_commands))

            if len(scrubber_commands) == 1:
                scrubber_rating = scrubber_commands[0]

        digit = digit + 1

    oxygen_rating_val = int(''.join([str(x) for x in oxygen_rating]), 2)
    scrubber_rating_val = int(''.join([str(x) for x in scrubber_rating]), 2)
    return oxygen_rating_val * scrubber_rating_val

def __get_counter(commands):
    counter = None
    for line in commands:
        if counter == None:
            counter = line.copy()
        else:
            counter = [sum(x) for x in zip(counter, line)]
    return counter