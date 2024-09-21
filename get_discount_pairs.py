# find biggest index <= x
def bin_search(arr, x):
    n = len(arr)
    if n == 1:
        if arr[0] <= x:
            return 0
        else:
            return -1
    else:
        mid = arr[n//2]
        if mid <= x:
            return bin_search(arr[n//2:], x) + n//2
        else:
            return bin_search(arr[:n//2], x)

def get_discount_pairs(x, prices):
    res = 0
    arr = list(map(lambda item: item % x, prices))
    arr.sort()
    idx_one = bin_search(arr, 0)
    if idx_one >= 1:
        res += (idx_one*(idx_one+1))//2
    arr = arr[idx_one+1:]
    arr_count = [] # count how many elements with a certain remainder
    arr_uniq = [] # unique remainder appeared
    cur_count = 0
    last_remainder = -1
    for i, elem in enumerate(arr):
        if elem != last_remainder and i != 0:
            arr_uniq.append(last_remainder)
            arr_count.append(cur_count)
            cur_count = 1
        else:
            cur_count += 1
        last_remainder = elem
    arr_count.append(cur_count)
    arr_uniq.append(last_remainder)
    l, r = 0, len(arr_uniq) - 1
    while l < r:
        s = arr_uniq[l] + arr_uniq[r]
        if s % x == 0:
            res += arr_count[l] * arr_count[r]
            l += 1
            r -= 1
        elif s < x:
            l += 1
        else: # s > x
            r -= 1
    return res

print(get_discount_pairs(3, [0, 0, 1, 1, 2, 2, 2]))
print(get_discount_pairs(60, [31, 25, 85, 29, 35]))
