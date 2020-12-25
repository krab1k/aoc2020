import itertools

data = []
with open('input.txt') as f:
    for line in f:
        data.append(int(line))


for i, j in itertools.combinations(range(len(data)), 2):
    if data[i] + data[j] == 2020:
        print(data[i] * data[j])
