def err_count_rec(error_string: str, x, y):
    exc_idx = error_string.find('!')
    if exc_idx != -1:
        error_string_0 = error_string[:exc_idx] + "0" + error_string[exc_idx+1:]
        error_string_1 = error_string[:exc_idx] + "1" + error_string[exc_idx+1:]
        return min(err_count_rec(error_string_0, x, y), err_count_rec(error_string_1, x, y)) % (10**9 + 7)
    else: # no !, start to count
        res = 0
        n_ones_before = 0
        n_zeros_before = 0
        for c in error_string:
            if c == "0": # count 10 error
                res = (res + n_ones_before*y) % (10**9 + 7)
                n_zeros_before += 1
            if c == "1":
                res = (res + n_zeros_before*x) % (10**9 + 7)
                n_ones_before += 1
        return res


def min_total_errors(error_string, x, y):
    return err_count_rec(error_string, x, y)

print(min_total_errors("101!1", 2, 3))
