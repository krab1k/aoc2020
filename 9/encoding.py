import itertools

data = []
with open('input.txt') as f:
    for line in f:
        data.append(int(line.strip()))


PREAMBLE_LENGTH = 25

for i in range(PREAMBLE_LENGTH, len(data)):
    found = False
    for j in range(i - PREAMBLE_LENGTH, i):
        for k in range(j + 1, i):
            if data[j] + data[k] == data[i]:
                found = True

    if not found:
        print(data[i])

