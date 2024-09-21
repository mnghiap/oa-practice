def find_requests_in_queue(wait):
    res = []
    t = 0
    while len(wait) > 0:        
        remove = []
        for i, wait_time in enumerate(wait):
            if wait_time <= t:
                remove.append(i)
        for idx in reversed(remove):
            wait.pop(idx)
        res.append(len(wait))
        if len(wait) > 0:
            wait.pop(0)
        t += 1
    return res + [0]

print(find_requests_in_queue([2, 2, 3, 1]))
