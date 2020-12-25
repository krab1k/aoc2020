import numpy as np
import functools
import re
from pprint import pprint
from copy import deepcopy


def generate_transformations(tiles):
    transformations = [
                lambda x: x,
                np.fliplr,
                np.flipud,
                functools.partial(np.rot90, k=1),
                functools.partial(np.rot90, k=2),
                functools.partial(np.rot90, k=3),
                lambda x: np.fliplr(np.rot90(x)),
                lambda x: np.flipud(np.rot90(x)),
            ]

    all_tiles = {}

    for tile_id, tile in tiles.items():
        all_tiles[tile_id] = [t(tile) for t in transformations]

    return all_tiles


def can_be_right(current, new):
    return (current[:,-1] == new[:, 0]).all()


def can_be_down(current, new):
    return (current[-1,:] == new[0, :]).all()


def can_be_assigned(plan, all_tiles, i, j, tile):
    if i == 0 and j == 0:
        return True
    elif i == 0:
        left_tile_id, left_tt = plan[i, j -1]
        if can_be_right(all_tiles[left_tile_id][left_tt], tile):
            return True
    elif j == 0:
        up_tile_id, up_tt = plan[i - 1, j]
        if can_be_down(all_tiles[up_tile_id][up_tt], tile):
            return True
    else:
        left_tile_id, left_tt = plan[i, j -1]
        up_tile_id, up_tt = plan[i - 1, j]
        if can_be_right(all_tiles[left_tile_id][left_tt], tile) and can_be_down(all_tiles[up_tile_id][up_tt], tile):
            return True

    return False


def locate_first(plan):
    n = len(plan)
    for i in range(n):
        for j in range(n):
            if plan[i][j] is None:
                return i, j


def solve(plan, all_tiles, available_tiles):
#    pprint(plan)
    if not available_tiles:
        return plan

    new_plan = np.copy(plan)
    i, j = locate_first(plan)
    for tile_id in available_tiles:
        for ti, tt in enumerate(all_tiles[tile_id]):
            if can_be_assigned(plan, all_tiles, i, j, all_tiles[tile_id][ti]):
                new_plan[i, j] = (tile_id, ti)
                new_available = set(available_tiles)
                new_available.remove(tile_id)
                res = solve(new_plan, all_tiles, new_available)
                if res is not None:
                    return res

    return None


def main():
    tiles = {}
    with open('input.txt') as f:
        data = f.read()
        for m in re.finditer('Tile (\d+):\n((?:.+\n)+)', data):
            tile_id = int(m.group(1))
            tile_str = m.group(2)
            lines = tile_str.split('\n')[:-1]
            size = len(lines)
            tile = np.zeros((size, size), dtype=int)
            for i, row in enumerate(lines):
                for j, col in enumerate(row):
                    if col == '#':
                        tile[i, j] = 1

            tiles[tile_id] = tile
    
    all_tiles = generate_transformations(tiles)

    plan_size = int(len(tiles) ** 0.5)
    plan = [[None] * plan_size] * plan_size

    available_tiles = set(all_tiles.keys())

    res_plan = solve(plan, all_tiles, available_tiles)
    print(res_plan[0][0][0] * res_plan[-1][0][0] * res_plan[0][-1][0] * res_plan[-1][-1][0])


if __name__ == '__main__':
    main()
