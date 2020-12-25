import itertools
import numpy as np


NEIGH = set(itertools.product((-1, 0, 1), repeat=4))
NEIGH.remove((0, 0, 0, 0))


def is_valid(i, j, k, l, A):
    x, y, z, w = A.shape
    return i >= 0 and j >= 0 and k >= 0 and l >= 0 and i < x and j < y and k < z and l < w


def evolve(A):
    B = np.copy(A)
    x, y, z, w = A.shape
    for i in range(x):
        for j in range(y):
            for k in range(z):
                for l in range(w):
                    s = 0
                    positions = [(i + n[0], j + n[1], k + n[2], l + n[3])for n in NEIGH if is_valid(i + n[0], j + n[1], k + n[2], l + n[3], A)]
                    for p in positions:
                        if A[p]:
                            s += 1
                    B[i, j, k, l] = False
                    if A[i, j, k, l]:
                        if (s == 2) or (s == 3):
                            B[i, j, k, l] = True
                    else:
                        if s == 3:
                            B[i, j, k, l] = True

    return B


def main():
    initial = []
    with open('input.txt') as f:
        for line in f:
            initial.append(line.strip())

    CYCLES = 6

    xsize = len(initial[0])
    ysize = len(initial)

    shape = (2 * CYCLES + xsize, 2 * CYCLES + ysize, 2 * CYCLES + 1, 2 * CYCLES + 1)
    A = np.zeros(shape=shape, dtype=bool)
    
    for i in range(xsize):
        for j in range(ysize):
            if initial[j][i] == '#':
                val = True
            else:
                val = False
            A[CYCLES + j, CYCLES + i, CYCLES, CYCLES] = val

    for i in range(CYCLES):
        A = evolve(A)

    print(np.sum(A))


if __name__ == '__main__':
    main()
