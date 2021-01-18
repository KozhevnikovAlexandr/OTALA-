import json
import random

with open('input.json', 'r') as read_file:
    input = json.load(read_file)

with open('output.json', 'r') as read_file:
    output = json.load(read_file)


def random_data(count, current_state='b1'):
    aut = {'b1': [[80, 'b4'], [40, 'b6']],
           'b2': [[80, 'b4'], [40, 'b6']],
           'b3': [[80, 'b4'], [40, 'b6']],
           'b4': [[72, 'b1'], [36, 'b7']],
           'b5': [[72, 'b1'], [36, 'b7']],
           'b6': [[72, 'b1'], [34, 'b2']],
           'b7': [[72, 'b1'], [33, 'b3']]}
    result = []
    for i in range(count):
        transition = aut[current_state][random.randint(0, 1)]
        result.append(transition[0])
        current_state = transition[1]
    return result


def get_data():
    result = []
    for i in range(len(input)):
        new_data = [0, 0, 0, 0]
        if input[i] == 0:
            new_data[0] = 1
        else:
            new_data[1] = 1
        if output[i] == 0:
            new_data[2] = 1
        else:
            new_data[3] = 1
        result.append(new_data)
    return result


def state_to_dec(state):
    state = ''.join(str(x) for x in state)
    number = 0
    len_dat = len(state)
    for i in range(len_dat):
        number += int(state[i]) * (2 ** (len_dat - i - 1))
    return number


if __name__ == '__main__':
    print(input[0])
    print(output[0])
    print(get_data()[0])
    print(state_to_dec(get_data()[0]))