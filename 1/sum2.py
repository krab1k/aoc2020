import itertools

data = []
with open('input.txt') as f:
    for line in f:
        data.append(int(line))


for i, j, k in itertools.combinations(range(len(data)), 3):
    if data[i] + data[j] + data[k] == 2020:
        print(data[i] * data[j] * data[k])
