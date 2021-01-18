from TimedAutomaton import TimedAutomaton
from Training import training
from modbus_data import get_modbus_data
import dpkt
from anomaly import *


def checking_transitions(ta, data, delays, acceptable_delay=100):
    success_count = 0
    anomalies = []
    state = data[0]
    for i in range(len(data)):
        new_state = data[i]
        previous_success_count = success_count
        anomaly_detected = False
        for transition in ta.transitions:
            if transition.source == state and transition.destination == new_state:
                if abs(delays[i] - transition.time) >= acceptable_delay:
                    anomalies.append(Anomaly([state, new_state], delays[i], 'time'))
                    anomaly_detected = True
                    break
                success_count += 1
                break
        if previous_success_count == success_count and not anomaly_detected:
            anomalies.append(Anomaly([state, new_state], delays[i], 'transition'))
        state = new_state
    return [success_count, anomalies]


if __name__ == '__main__':
    print("Начата выгрузка данных для обучения ")
    ta = TimedAutomaton([0, 1])
    data = get_modbus_data('modbus_clever_office_131-218_full_bad.pcap', '192.168.12.131', '192.168.252.218', 6)
    pcapReader = dpkt.pcap.Reader(open('modbus_clever_office_131-218_full_bad.pcap', "rb"))
    raw_delays = []
    second = False
    time_for_current_state = 0
    for i, j in pcapReader:
        if second:
            time_for_current_state += i
            raw_delays.append(time_for_current_state)
            time_for_current_state = 0
            second = False
        else:
            second = True
            time_for_current_state = i
    pr_time = raw_delays[0]
    delays = []
    for i in range(2, len(raw_delays) - 1):
        delays.append(raw_delays[i] - pr_time)
        pr_time = raw_delays[i]
        i += 1
    print("Данные выгружены ")
    working_data = data[3000:]
    print("Обучение начато")
    ta = training(ta, data[:1000], delays, convergence_number=100)
    print("Обучение завершено")
    result = checking_transitions(ta, working_data, delays)
    print('=' * 10)
    print('РЕЗУЛЬТАТЫ: ')
    print('Данных для обучения: ' + str(len(data) - len(working_data)))
    print('Данных для проверки: ' + str(len(working_data)))
    print('Успехов ' + str(result[0]))
    print('Аномалий ' + str(len(result[1])))
    if len(result[1]) > 0:
        print('АНОМАЛИИ: ')
        shown_anomalies = 0
        for i in result[1]:
            if i.anomaly_type == AnomalyType.non_existent_transition:
                print('... несуществующий переход' + str(i.transition))
            else:
                print('... ошибка веремнеи в переходе' + str(i.transition))
            shown_anomalies += 1
            if shown_anomalies >= 10:
                print('... и ещё ' + str(len(result[1]) - 10) + ' аномалий')
                break
    print('Процент успеха ' + str(result[0]/len(working_data) * 100) + '%')