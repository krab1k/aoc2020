import itertools
import numpy as np


NEIGH = set(itertools.product((-1, 0, 1), repeat=3))
NEIGH.remove((0, 0, 0))



def pprint(A):
    x, y, z = A.shape
    for i in range(z):
        for j in range(x):
            for k in range(y):
                if A[j, k, i]:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print('\n')


def is_valid(i, j, k, A):
    x, y, z = A.shape
    return i >= 0 and j >= 0 and k >= 0 and i < x and j < y and k < z


def evolve(A):
    B = np.copy(A)
    x, y, z = A.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                s = 0
                positions = [(i + n[0], j + n[1], k + n[2])for n in NEIGH if is_valid(i + n[0], j + n[1], k + n[2], A)]
                for p in positions:
                    if A[p]:
                        s += 1
                B[i, j, k] = False
                if A[i, j, k]:
                    if (s == 2) or (s == 3):
                        B[i, j, k] = True
                else:
                    if s == 3:
                        B[i, j, k] = True


    return B


def main():
    initial = []
    with open('input.txt') as f:
        for line in f:
            initial.append(line.strip())

    print(initial)

    CYCLES = 6

    xsize = len(initial[0])
    ysize = len(initial)

    shape = (2 * CYCLES + xsize, 2 * CYCLES + ysize, 2 * CYCLES + 1)
    A = np.zeros(shape=shape, dtype=bool)
    
    for i in range(xsize):
        for j in range(ysize):
            if initial[j][i] == '#':
                val = True
            else:
                val = False
            A[CYCLES + j, CYCLES + i, CYCLES] = val

    pprint(A)

    for i in range(CYCLES):
        A = evolve(A)
        pprint(A)

    print(np.sum(A))

if __name__ == '__main__':
    main()
