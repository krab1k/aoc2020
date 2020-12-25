data = []
with open('input.txt') as f:
    for line in f:
        data.append(line.strip())

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

width = len(data[0])

total_trees = 1

for dx, dy in slopes:
    col = 0
    trees = 0
    for i in range(0, len(data), dy):
        if data[i][col % width] == '#':
            trees += 1

        col += dx
    total_trees *= trees

print(total_trees)
