def find_recurring_names(real_names, all_names):
    name_to_hash = {name: frozenset(name).__hash__() for name in real_names}
    hash_to_name = {hash_name: name for name, hash_name in name_to_hash.items()}
    name_count = {hash_name: 0 for hash_name in hash_to_name}
    res = []
    for acc_name in all_names:
        name_count[frozenset(acc_name).__hash__()] += 1
    for name_hash in name_count:
        if name_count[name_hash] > 1:
            res.append(hash_to_name[name_hash])
    return sorted(res)

print(find_recurring_names(["rohn", "henry", "daisy"], ["ryhen", "aisyd", "henry"]))
print(find_recurring_names(["tom", "jerry"], ["reyjr", "mot", "tom", "jerry", "mto"]))
