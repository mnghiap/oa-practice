def palindrome(x):
    return x == x[::-1]

def count_distinct_passwords(password):
    prev_res = 1
    char_idxs = dict()
    for k, c in enumerate(password):
        if not c in char_idxs:
            char_idxs[c] = [k]
        else:
            char_idxs[c].append(k)
    for i in range(1, len(password)):
        res = prev_res + i
        last = password[i]
        last_idxs = [j for j in char_idxs[last] if j < i]
        res -= len(last_idxs)
        prev_res = res
    return res

print(count_distinct_passwords("abc")) # 4
print(count_distinct_passwords("abaa")) # 4
print(count_distinct_passwords("aaaaaaaaaaaaaaaaa"))
