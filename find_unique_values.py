def find_unique_values(experience):
    experience.sort()
    comb = []
    for i in range(len(experience)//2):
        comb.append(experience[i] + experience[len(experience) - 1 - i])
    return len(set(comb))

print(find_unique_values([1, 4, 1, 3, 5, 6]))
print(find_unique_values([1, 1, 1, 1, 1, 1]))
print(find_unique_values([1, 100, 10, 1000]))
