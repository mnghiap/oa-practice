def get_min_num_moves(blocks):
    idx_min, idx_max = blocks.index(min(blocks)), blocks.index(max(blocks))
    if idx_min < idx_max:
        return idx_min + len(blocks) - 1 - idx_max
    else:
        return idx_min + len(blocks) - 1 - (idx_max + 1)
    
print(get_min_num_moves([2, 4, 3, 1, 6]))
print(get_min_num_moves([4, 11, 9, 10, 12]))
