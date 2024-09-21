import math

def number_of_suitable_locations(center, d):
    center.sort()
    dh = d/2
    res = 0
    n = len(center)
    # case 1: x < c0
    sum_c = sum(center)
    res += max(0, center[0]-math.ceil((sum_c - dh)/n))
    # case 2: c(n-1) <= x
    res += max(0, math.floor((dh + sum_c)/n) - center[-1] + 1)
    # case 3: c(k) <= x < c(k+1) for some k
    for k in range(n-1):
        sum_c_0_k = sum(center[0:k+1])
        if 2*k+2 == n and sum_c - 2*sum_c_0_k <= dh:
            res += center[k+1] - center[k]
        elif 2*k+2 > n:
            strict_upper_bound = math.floor((dh - sum_c +2*sum_c_0_k)/(2*k + 2 - n))
            if strict_upper_bound < center[k]:
                res += 0
            else:
                max_bound = min(strict_upper_bound, center[k+1] - 1)
                res += (max_bound - center[k] + 1)
        else: # 2k+2 < n
            strict_lower_bound = math.ceil((sum_c - 2*sum_c_0_k -dh)/(n - 2*k -2))
            if strict_lower_bound > center[k+1] - 1:
                res += 0
            else:
                min_bound = max(strict_lower_bound, center[k])
                res += (center[k+1] - min_bound)
    return res

print(number_of_suitable_locations([-2, 1, 0], 8))
