import itertools

data = []
with open('input.txt') as f:
    for line in f:
        data.append(int(line.strip()))


PREAMBLE_LENGTH = 25

idx = None
for i in range(PREAMBLE_LENGTH, len(data)):
    found = False
    for j in range(i - PREAMBLE_LENGTH, i):
        for k in range(j + 1, i):
            if data[j] + data[k] == data[i]:
                found = True

    if not found:
        idx = i
        break


n = data[idx]
for i in range(idx):
    for j in range(i + 1, idx):
        if sum(data[i:j]) == n:
            print(min(data[i:j]) + max(data[i:j]))
