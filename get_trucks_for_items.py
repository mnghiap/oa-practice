# biggest index such that arr[idx] <= x
def bin_search(arr, x, key):
    n = len(arr)
    if n == 1:
        if key(arr[0]) <= x:
            return 0
        else:
            return -1
    else:
        mid = key(arr[n//2])
        if mid <= x:
            return n//2 + bin_search(arr[n//2:], x, key)
        else:
            return bin_search(arr[:n//2], x, key)

def get_trucks_for_items(trucks, items):
    res = []
    trucks = [(truck, i) for i, truck in enumerate(trucks)]
    trucks.sort(key=lambda x: x[0])
    for it in items:
        idx = bin_search(trucks, it, key=lambda x: x[0])
        if idx != -1:
            if idx+1 < len(trucks):
                res.append(trucks[idx+1][1])
            else:
                res.append(-1)
        else:
            res.append(trucks[0][1])
    return res

print(get_trucks_for_items([4, 5, 7, 2], [1, 2, 5]))
print(get_trucks_for_items([5, 3, 8, 1], [6, 10]))
print(get_trucks_for_items([1, 3, 5, 2, 3, 2], [1, 2, 3]))
