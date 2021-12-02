def read_input(filename):
    with open(filename) as infile:
        instructions = [x.strip("\n").split(" ") for x in infile]
        return instructions


def get_end_position(instructions, include_aim=False):
    current_x = 0
    current_y = 0
    current_aim = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        # Up & Down will only change current_y, Forward & Backward will only change current_x value
        if include_aim is False:
            if direction == "up":
                current_y -= distance
            if direction == "down":
                current_y += distance
            if direction == "forward":
                current_x += distance
            if direction == "back":
                current_y += distance

        # include_aim will make Up & Down change the value of current_aim rather than current_y
        # Forward & Backward will now change current_x and current_y * current_aim
        if include_aim is True:
            if direction == "up":
                current_aim -= distance
            if direction == "down":
                current_aim += distance
            if direction == "forward":
                current_x += distance
                current_y += distance * current_aim
            if direction == "back":
                current_x -= distance
                current_y -= distance * current_aim

    return current_x * current_y


day_two_data = read_input("aoc_2_input.txt")

part_one_answer = get_end_position(day_two_data)
print("Part One: {}".format(part_one_answer))

part_two_answer = get_end_position(day_two_data, include_aim=True)
print("Part Two: {}".format(part_two_answer))

