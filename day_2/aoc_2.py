def read_input(filename):
    with open(filename) as infile:
        instructions = [x.strip("\n").split(" ") for x in infile]
        return instructions


def get_end_position(instructions, include_aim):
    current_x = 0
    current_y = 0
    current_aim = 0
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1])
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

part_one_answer = get_end_position(day_two_data, False)
print("Part One: {}".format(part_one_answer))

part_two_answer = get_end_position(day_two_data, True)
print("Part Two: {}".format(part_two_answer))

