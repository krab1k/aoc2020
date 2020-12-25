from copy import deepcopy

neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def pprint(layout):
    for i in range(len(layout)):
        print(''.join(layout[i]))
    print('\n')


def is_valid(layout, i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(layout) or j >= len(layout[i]):
        return False

    return True


def is_vector_occupied(layout, i, j, di, dj):
    ii = i + di
    jj = j + dj

    occupied = False
    while is_valid(layout, ii, jj):
        if layout[ii][jj] == '#':
            occupied = True
            break
        elif layout[ii][jj] == 'L':
            break

        ii += di
        jj += dj

    return occupied


def can_occupy(layout, i, j):
    for di, dj in neighbours:
        if is_vector_occupied(layout, i, j, di, dj):
            return False

    return True


def can_empty(layout, i, j):
    occupied = 0
    for di, dj in neighbours:
        if is_vector_occupied(layout, i, j, di, dj):
            occupied += 1

    return occupied >= 5


def evolve(layout):
    new_state = deepcopy(layout)

    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == 'L':
                if can_occupy(layout, i, j):
                    new_state[i][j] = '#'
            elif layout[i][j] == '#':
                if can_empty(layout, i, j):
                    new_state[i][j] = 'L'

    return new_state


def main():
    layout = []
    with open('input.txt') as f:
        for line in f:
            layout.append(list(line.strip()))

    pprint(layout)

    new_state = evolve(layout)
    pprint(new_state)
    while new_state != layout:
        layout = deepcopy(new_state)
        new_state = evolve(layout)
        pprint(new_state)

    s = 0
    for i in range(len(layout)):
        for j in range(len(layout[i])):
            if layout[i][j] == '#':
                s += 1

    print(s)


if __name__ == '__main__':
    main()
