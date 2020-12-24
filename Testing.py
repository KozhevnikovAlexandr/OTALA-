from TimedAutomaton import TimedAutomaton
import test_data_constructor
from Training import training
from modbus_data import get_modbus_data

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
    data = get_modbus_data('modbus_40-3_unordered.pcap', '192.168.0.40', '192.168.0.3', 62)
    data1 = get_modbus_data('modbus_clever_office_131-218_full_bad.pcap', '192.168.12.131', '192.168.252.218', 6)
    ta = training(ta, data[:300], convergence_number=100)
    working_data = data[300:]
    result = checking_transitions(ta, working_data)
    print('успехов ' + str(result[0]))
    print('аномалий ' + str(result[1]))
    print('процент успеха ' + str(result[0] / len(working_data) * 100))
