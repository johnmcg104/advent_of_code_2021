def read_input(filename):
    with open(filename) as infile:
        data = [x.strip("\n") for x in infile]
        return data


def transpose_data(data):
    return list(zip(*data))


def get_gamma_epsilon(data):
    gamma = []
    epsilon = []
    for entry in data:
        ones = entry.count('1')
        zeros = entry.count("0")
        if ones > zeros:
            gamma.append(max("1"))
            epsilon.append(max("0"))
        if zeros > ones:
            gamma.append(max("0"))
            epsilon.append(max("1"))

    # Join the lists and convert to decimal
    gamma = "".join(gamma)
    epsilon = "".join(epsilon)
    return gamma, epsilon


def get_decimal_mult(gamma, epsilon):
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    return gamma_dec * epsilon_dec


def get_scrubber_ratings(data, gamma, epsilon):
    pass


day_three_data = read_input("aoc_3_input.txt")
transposed = transpose_data(day_three_data)
gamma = get_gamma_epsilon(transposed)[0]
epsilon = get_gamma_epsilon(transposed)[1]
part_one_answer = get_decimal_mult(gamma, epsilon)
print("Part one: {}".format(part_one_answer))



