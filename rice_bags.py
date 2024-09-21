# ah here we go again
# find x
import sys
sys.setrecursionlimit(10)
def bin_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1:
        if arr[0] == x:
            return 0
        else:
            return -1
    else:
        mid = arr[n//2]
        if mid <= x:
            idx = bin_search(arr[n//2:], x)
            if idx == -1:
                return -1
            else:
                return n//2 + idx
        else:
            return bin_search(arr[:n//2], x)

def max_set_size(rice_bags):
    rice_bags.sort()
    chains = []
    while len(rice_bags) > 0:
        x = rice_bags.pop(0)
        chains.append([x])
        if len(rice_bags) == 0:
            break
        while True:
            idx_next = bin_search(rice_bags, x*x)
            if idx_next == -1:
                break
            else:
                rice_bags.pop(idx_next)
                chains[-1].append(x*x)
                x = x*x
    res = max(map(lambda x: len(x), chains))
    return res

print(max_set_size([3, 9, 4, 2, 16]))
print(max_set_size([1, 3, 5, 7, 49]))
