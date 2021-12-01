def read_input(filename):
    with open(filename) as infile:
        values = [int(value.strip("\n")) for value in infile if value.strip("\n").isdigit()]
        return values


def get_increases(input_data):
    # Compare current element in a list with the previous element. Increase counter if it is larger
    increase_counter = 0
    for previous, current in zip(input_data, input_data[1:]):
        if current > previous:
            increase_counter += 1
    return increase_counter


def get_sliding_averages(input_data):
    # Make a list of the three measurement sliding averages
    averages = []
    for (first, second, third) in zip(input_data, input_data[1:], input_data[2:]):
        average = (first + second + third) / 3
        averages.append(average)
    return averages


input_values = read_input("aoc_1_input.txt")

sequential_increases = get_increases(input_values)
print("Part One: {}".format(sequential_increases))

sliding_averages = get_sliding_averages(input_values)
sliding_increases = get_increases(sliding_averages)
print("Part Two: {}".format(sliding_increases))
