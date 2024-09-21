def find_maximum_maximumcount(categories):
    chars = set(categories)
    count = {char: 0 for char in chars}
    max_count = {char: 0 for char in chars}
    for i, char in enumerate(categories):
        count[char] += 1
        max_chars = [char for char in max_count if count[char] == max(count.values())]
        for max_char in max_chars:
            max_count[max_char] += 1
    return max(max_count.values())

print(find_maximum_maximumcount("bccaaacb"))
print(find_maximum_maximumcount("zzzz"))
