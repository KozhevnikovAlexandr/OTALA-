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
    return [success_count, anomalies]


def cheching_result(ta, data):
    success_count = 0
    anomalies = 0
    current_state = data[0]
    for new_state in data:
        ps = success_count
        for transition in ta.transitions:
            if transition.source == current_state and transition.destination[0] == new_state[0] and \
                    transition.destination[1] == new_state[1]:
                success_count += 1
                current_s   tate = new_state
                break
        if success_count == ps:
            anomalies += 1
        return [success_count, anomalies]


if __name__ == '__main__':
    ta = TimedAutomaton([0, 1])
    data = [test_data_constructor.state_to_dec(x) for x in test_data_constructor.get_data()]
    ta = training(ta, data, convergence_number=100)
    print(checking_transitions(ta, data))
