import json

with open('input.json', 'r') as read_file:
    input = json.load(read_file)

with open('output.json', 'r') as read_file:
    output = json.load(read_file)

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