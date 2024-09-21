def check_anagram(a, b):
    if len(a) != len(b):
        return False
    else:
        return sorted(a) == sorted(b)

def remove_anagram(text_list):
    name_hash = dict()
    remove = []
    for i, text in enumerate(text_list):
        if frozenset(text) not in name_hash:
            name_hash[frozenset(text)] = text
        else:
            ref = name_hash[frozenset(text)]
            if check_anagram(ref, text):
                remove.append(text)
    return sorted(list(set(text_list) - set(remove)))

print(remove_anagram(["code", "doce", "ecod", "framer", "frame"]))
