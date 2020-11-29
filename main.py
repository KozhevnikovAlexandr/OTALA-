import json
from TimedAutomaton import TimedAutomaton

convergence_number = 100

ta = TimedAutomaton([0, 1])

with open('input.json', 'r') as read_file:
    input = json.load(read_file)

with open('output.json', 'r') as read_file:
    output = json.load(read_file)

work_input = input[:500]
work_output = output[:500]

data = [list(tup) for tup in zip(work_input, work_output)]
test_data = [['a', 3], ['b', 2], ['b', 2], ['a', 3], ['a', 3]]

currentState = ta.create_new_state(data[0])
stateExist = False
changes = 0
n_conv = 0
state_count = 1
transition_count = 0
observation_count = 0
time_was_changed = False
time = 0

for new_observation in data:
    observation_count += 1
    for state in ta.states:
        if new_observation == state:
            stateExist = True
            transition = ta.find_transition(currentState, state)
            if transition:
                time_was_changed = ta.adapt_timing_information(transition, time)
            else:
                ta.create_new_transition(currentState, time, state)
            currentState = state
    if not stateExist:
        s_new = ta.create_new_state(new_observation)
        ta.create_new_transition(currentState, time, s_new)
        currentState = s_new
    stateExist = False
    if n_conv > convergence_number:
        break
    if transition_count == len(ta.transitions) and state_count == len(ta.states) and not time_was_changed:
        n_conv += 1
    else:
        n_conv = 0
    time_was_changed = False
    state_count = len(ta.states)
    transition_count = len(ta.transitions)

print('Изучено данных: '+ str(observation_count))
print('Состояний: ' + str(len(ta.states)))
print('Переходов: ' + str(len(ta.transitions)))
print('*' * 10 + 'ТЕСТ' + '*' * 10)
test_input = input[500:]
test_output = output[500:]
success = 0

for i in range(len(test_input)):
    a = ta.get_result(test_input[i])
    if a == test_output[i]:
        success += 1

print('верно предсказано: ' + str(success))
print('всего проверок: ' + str(len(input) - observation_count))
print('процент успеха: ' + str(success/(len(input) - observation_count)*100))