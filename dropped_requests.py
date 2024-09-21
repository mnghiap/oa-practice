def dropped_requests(request_time):
    req_per_sec = []
    last_t = 0
    cum_req = 0 
    for req in request_time:
        if req != last_t:
            req_per_sec.append(cum_req)
            if req - last_t > 1:
                req_per_sec += [0]*(req - last_t -1)
            cum_req = 1
            last_t = req
        else:
            cum_req += 1
    req_per_sec.append(cum_req)
    
    rm_rq_1sec = [0] * len(req_per_sec)
    rm_rq_10sec = [0] * len(req_per_sec)
    rm_rq_60sec = [0] * len(req_per_sec)
    for sec, num_req in enumerate(req_per_sec):
        # check 1 sec requirement
        if num_req > 3:
            rm_rq_1sec[sec] = num_req - 3
        # check 10 sec requirement
        num_req_last_10sec = sum(req_per_sec[max(sec-9, 1):sec+1])
        if num_req_last_10sec > 20:
            rm_rq_10sec[sec] = min(num_req, num_req_last_10sec - 20)
        # check 60 sec requirement
        num_req_last_60sec = sum(req_per_sec[max(sec-59, 1):sec+1])
        if num_req_last_60sec > 60:
            rm_rq_60sec[sec] = min(num_req, num_req_last_60sec - 60)
    dropped = sum(map(lambda x: max(x), zip(rm_rq_1sec, rm_rq_10sec, rm_rq_60sec)))
    return dropped


print(dropped_requests([1, 1, 1, 1, 2]))
print(dropped_requests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]))
print(dropped_requests([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]))
