def get_longest_match(text, regex):
    star_idx = regex.find("*")
    if len(regex) == 1:
        return len(text)
    if star_idx == 0:
        rest = regex[1:]
        rest_start_idx = text.find(rest)
        if rest_start_idx == -1:
            return -1
        else:
            return rest_start_idx + len(rest)
    elif star_idx == len(regex) - 1:
        rest = regex[:-1]
        rest_start_idx = text.find(rest)
        if rest_start_idx == -1:
            return -1
        else:
            return len(text) - rest_start_idx
    else: # star is in middle
        left, right = regex[:star_idx], regex[star_idx+1:]
        left_start_idx, right_start_idx = text.find(left), text.rfind(right)
        if left_start_idx + len(left) >= right_start_idx:
            return -1
        else:
            return right_start_idx + len(right) - left_start_idx
        
print(get_longest_match("hackerrank", "ack*r"))
print(get_longest_match("abdcf", "abd*dcf"))
print(get_longest_match("abcdefgh", "*def"))
print(get_longest_match("abcdefgh", "efg*"))
print(get_longest_match("abcdefgh", "*"))
