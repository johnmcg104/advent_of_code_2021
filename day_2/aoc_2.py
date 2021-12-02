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
        amount = int(instruction[1])
        # If include_aim is True, Up & Down will change the value of current_aim
        # If include_aim is False, Up & Down will change current_y instead
        if direction == "up":
            if include_aim:
                current_aim -= amount
            else:
                current_y -= amount
        if direction == "down":
            if include_aim:
                current_aim += amount
            else:
                current_y += amount
        # If include_aim is True, forward & backward will change current_x, and current_y * current_aim
        # If include_aim is False, forward & backward will only change current_x value
        if direction == "forward":
            if include_aim:
                current_x += amount
                current_y += amount * current_aim
            else:
                current_x += amount
        if direction == "back":
            if include_aim:
                current_x -= amount
                current_y -= amount * current_aim
            else:
                current_y += amount

    return current_x * current_y


day_two_data = read_input("aoc_2_input.txt")

part_one_answer = get_end_position(day_two_data)
print("Part One: {}".format(part_one_answer))

part_two_answer = get_end_position(day_two_data, include_aim=True)
print("Part Two: {}".format(part_two_answer))

