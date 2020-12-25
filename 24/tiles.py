from pprint import pprint

dirs = {'e' : (1, 0),
        'se': (0.5, 1),
        'sw': (-0.5, 1),
        'w' : (-1, 0),
        'nw': (-0.5, -1),
        'ne': (0.5, -1)}


def main():
    tiles = []
    with open('input.txt') as f:
        for line in f:
            tile = []
            rest = line.strip()
            while rest:
                for d in dirs:
                    if rest.startswith(d):
                        tile.append(d)
                        rest = rest[len(d):]
                        break
            tiles.append(tile)

    flipped = set()
    for tile in tiles:
        x, y = 0, 0
        for d in tile:
            dx, dy = dirs[d]
            x += dx
            y += dy
        if (x, y) not in flipped:
            flipped.add((x, y))
        else:
            flipped.remove((x, y))

    print(len(flipped))
    
if __name__ == '__main__':
    main()
