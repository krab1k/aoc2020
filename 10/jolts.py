data = []
with open('input.txt') as f:
    for line in f:
        data.append(int(line.strip()))

data.sort()

diff = {1: 0, 2: 0, 3: 0}

input_jolts = 0

current = input_jolts
for i in range(len(data)):
    diff[data[i] - current] += 1
    current = data[i]

print(diff[1] * (diff[3] + 1))

