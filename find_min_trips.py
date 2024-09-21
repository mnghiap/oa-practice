def find_min_trips(packageweight):
    num_pkt_weight_dict = dict()
    res = 0
    for i in range(len(packageweight)):
        num_pkt_weight_dict[packageweight[i]] = num_pkt_weight_dict.get(packageweight[i], 0) + 1
    for weight in num_pkt_weight_dict:
        num_pkt_weight = num_pkt_weight_dict[weight]
        if num_pkt_weight == 1:
            return -1
        if num_pkt_weight == 2:
            res += 1
        elif num_pkt_weight % 3 == 0:
            res += num_pkt_weight // 3
        elif num_pkt_weight % 3 == 1:
            res += 1 + (num_pkt_weight - 1) // 3
        else:
            res += 2 + (num_pkt_weight - 4) // 3
    return res

print(find_min_trips([3, 4, 4, 3, 1]))
