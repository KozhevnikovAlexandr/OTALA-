from scapy.all import rdpcap
import test_data_constructor

def get_modbus_data(path, input_ip, output_ip, displacement):
    pcap = rdpcap(path)
    input_data = dict()
    output_data = dict()
    input_count = 0
    output_count = 0
    for i in pcap.res:
        new_data = i['Raw'].load[displacement:]
        if i['IP'].src == input_ip and new_data not in input_data.keys():
            input_data[new_data] = input_count
            input_count += 1
        elif i['IP'].src == output_ip and new_data not in output_data.keys():
            output_data[new_data] = output_count
            output_count += 1
    queue = []
    res = []
    for i in pcap.res:
        new_data = i['Raw'].load[displacement:]
        if i['IP'].src == input_ip:
            new_observation = [0] * (input_count+output_count)
            new_observation[input_data[new_data]] = 1
            queue.append(new_observation)
        elif i['IP'].src == output_ip:
            if len(queue) == 0:
                continue
            new_observation = queue[0]
            queue = queue[1:]
            new_observation[output_data[new_data] + input_count] = 1
            res.append(test_data_constructor.state_to_dec(new_observation))
    return res