
data = []
with open('input.txt') as f:
    for line in f:
        data.append(line.strip())


width = len(data[0])

col = 0
trees = 0
for i in range(len(data)):
    if data[i][col % width] == '#':
        trees += 1

    col += 3


print(trees)
