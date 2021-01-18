from enum import Enum


class AnomalyType(Enum):
    non_existent_transition = 1
    time_lag = 2


class Anomaly:
    transition = []
    anomaly_type = []
    delay = 0

    def __init__(self, transition, delay, anomaly_type):
        self.delay = delay
        self.transition = transition
        if anomaly_type == 'transition':
            self.anomaly_type = AnomalyType.non_existent_transition
        if anomaly_type == 'time_lag':
            self.anomaly_type = AnomalyType.time_lag

'''
abs(transition.time - delays[i]) <= 1
    print("Начата выгрузка данных для обучения ")
    ta = TimedAutomaton([0, 1])
    data = get_modbus_data('modbus_40-3_unordered.pcap', '192.168.0.40', '192.168.0.3', 62)
    data = get_modbus_data('modbus_clever_office_131-218_full_bad.pcap', '192.168.12.131', '192.168.252.218', 6)
    pcapReader = dpkt.pcap.Reader(open('modbus_clever_office_131-218_full_bad.pcap', "rb"))
    delays = [0] * 5000
    print("Данные выгружены ")
    data1 = test_data_constructor.random_data(100)
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
        c = 0
        for i in result[1]:
            print('... несуществующий переход' + str(i))
            c += 1
            if c >= 10:
                print('... и ещё ' + str(len(result[1]) - 10) + ' аномалий')
                break
    print('Процент успеха ' + str(result[0]/len(working_data) * 100) + '%')'''