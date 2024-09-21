# one more time! daft punk
# always return biggest index idx <= x
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
            return n//2 + bin_search(arr[n//2:], x)
        else:
            return bin_search(arr[:n//2], x)

# def get_min_distance(center, destination):
#     destination.sort()
#     res = 0
#     for c in center:
#         idx = bin_search(destination, c)
#         print(c, idx)
#         if idx == -1:
#             res += abs(destination[0] - c)
#         elif idx == len(destination) - 1:
#             res += abs(destination[-1] - c)
#         else:
#             res += min(abs(destination[idx] - c), abs(destination[idx+1] - c))
#     return res
        
def get_min_distance(center, destination):
    destination.sort()
    center.sort()
    res = 0
    while len(center) > 0:
        c = center.pop(0)
        idx = bin_search(destination, c)
        if idx == -1:
            res += abs(destination[0] - c)
            c_idx = 0
        elif idx == len(destination) - 1:
            res += abs(destination[-1] - c)
            c_idx = len(destination) - 1
        else:
            if abs(destination[idx] - c) < abs(destination[idx+1] - c):
                c_idx = idx
            else:
                c_idx = idx+1
            res += min(abs(destination[idx] - c), abs(destination[idx+1] - c))
        destination.pop(c_idx)
    return res

print(get_min_distance([1, 2, 2], [5, 2, 4])) # 6
print(get_min_distance([1, 2, 3, 4], [3, 2, 4, 1])) # 0
