def maximum_final(arr):
    amin, amax, alen = min(arr), max(arr), len(arr)
    if amax - amin >= amin + alen - 1:
        return amin + alen - 1 
    else:
        return amax
    
print(maximum_final([3, 1, 3, 4]))
print(maximum_final([1, 2, 3, 4, 5, 7]))
    