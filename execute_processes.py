import math

def total_execution_time(execution):
    total_time = 0
    time_to_proc = dict()
    proc_to_group = dict()
    for i, time in enumerate(execution):
        if time not in time_to_proc:
            time_to_proc[time] = set([i])
        else:
            time_to_proc[time].add(i)
    for groups in time_to_proc.values():
        for proc in groups:
            proc_to_group[proc] = groups
    for i, time in enumerate(execution):
        total_time += time
        for proc in proc_to_group[i]:
            if execution[proc] == time:
                execution[proc] = math.ceil(execution[proc] / 2)
    return total_time

print(total_execution_time([5, 5, 3, 6, 5, 3]))
