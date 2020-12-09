from TimedAutomaton import TimedAutomaton
import test_data_constructor
from Training import training


def checking_transitions(ta, data):
    success_count = 0
    anomalies = 0
    state = data[0]
    for new_state in data:
        previous_success_count = success_count
        for transition in ta.transitions:
            if transition.source == state and transition.destination == new_state:
                success_count += 1
                state = new_state
                break
        if success_count == previous_success_count:
            anomalies += 1
        state = new_state
    return [success_count, anomalies]


if __name__ == '__main__':
    ta = TimedAutomaton([0, 1])
    data = [test_data_constructor.state_to_dec(x) for x in test_data_constructor.get_data()]
    ta = training(ta, data, convergence_number=100)
    result = checking_transitions(ta, data)
    print('успехов ' + str(result[0]))
    print('аномалий ' + str(result[1]))
    print('процент успеха ' + str(result[0] / len(data) * 100))
