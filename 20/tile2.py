import numpy as np
import functools
import re
from pprint import pprint
from copy import deepcopy


MONSTER = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']


TRANSFORMATIONS = [
                lambda x: x,
                np.fliplr,
                np.flipud,
                functools.partial(np.rot90, k=1),
                functools.partial(np.rot90, k=2),
                functools.partial(np.rot90, k=3),
                lambda x: np.fliplr(np.rot90(x)),
                lambda x: np.flipud(np.rot90(x)),
            ]


def get_tile_from_str(string):
    n = len(string)
    m = len(string[0])
    tile = np.zeros((n, m), dtype=int)
    for i, row in enumerate(string):
        for j, col in enumerate(row):
            if col == '#':
                tile[i, j] = 1
    return tile


def generate_transformations(tiles):
    all_tiles = {}
    for tile_id, tile in tiles.items():
        all_tiles[tile_id] = [t(tile) for t in TRANSFORMATIONS]

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


def reconstruct_image(plan, all_tiles, plan_size, tile_size):
    m = tile_size - 2
    n = plan_size * m
    image = np.empty((n, n), dtype=int)
    for i in range(plan_size):
        for j in range(plan_size):
            tile_id, tt = plan[i][j]
            image[i * m: (i + 1) * m, j * m: (j + 1) * m] = all_tiles[tile_id][tt][1: -1, 1: -1]

    return image


def find_monster(image, monster_tile):
    x, y = image.shape
    m, n = monster_tile.shape

    monster_size = np.sum(monster_tile)

    for t in TRANSFORMATIONS:
        t_image = t(image)
        found = False
        for i in range(x - m + 1):
            for j in range(y - n + 1):
                if monster_size == np.sum(t_image[i: i + m, j: j + n] & monster_tile):
                    found = True
                    t_image[i: i + m, j: j + n] -= monster_tile

        if found:
            break
    else:
        print('Error: Not found in image')

    return np.sum(t_image)


def main():
    np.set_printoptions(linewidth=350, threshold=10000)
    tiles = {}
    with open('input.txt') as f:
        data = f.read()
        for m in re.finditer('Tile (\d+):\n((?:.+\n)+)', data):
            tile_id = int(m.group(1))
            tile_str = m.group(2)
            tile = get_tile_from_str(tile_str.split('\n')[:-1])
            tiles[tile_id] = tile
    
    all_tiles = generate_transformations(tiles)

    plan_size = int(len(tiles) ** 0.5)
    plan = [[None] * plan_size] * plan_size

    available_tiles = set(all_tiles.keys())

    res_plan = solve(plan, all_tiles, available_tiles)
    image = reconstruct_image(res_plan, all_tiles, plan_size, tile.shape[0])

    monster_tile = get_tile_from_str(MONSTER)
    res = find_monster(image, monster_tile)

    print(res)


if __name__ == '__main__':
    main()
