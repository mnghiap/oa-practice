def group_students(levels, max_spread):
    levels.sort()
    groups = 0
    for i, lvl in enumerate(levels):
        if i == 0 or (lvl - cur_min) > max_spread:
            groups += 1
            cur_min = lvl
    return groups

print(group_students([1, 4, 7, 3, 4], 2))
print(group_students([1, 3, 5, 7, 9], 1))
