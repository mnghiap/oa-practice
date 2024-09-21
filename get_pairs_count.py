# let's do this efficiently :)
# O(n log n)

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

def get_pairs_count(process, k):
    process.sort()
    res = 0
    while(len(process)) > 1:
        first = process[0]
        idx = bin_search(process, first+k, 0)
        res += idx
        process.pop(0)
    return res

print(get_pairs_count([100, 200, 300, 400], 250)) # 5
print(get_pairs_count([10, 12, 11], 0)) # 0
print(get_pairs_count([7, 10, 13, 11], 3)) # 4
