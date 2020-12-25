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

    for day in range(100):
        to_flip = set()
        for x, y in flipped:
            neighbours = 0
            for dx, dy in dirs.values():
                if (x + dx, y + dy) in flipped:
                    neighbours += 1

            if neighbours == 0 or neighbours > 2:
                to_flip.add((x, y))

        whites = set()
        for x, y in flipped:
            for dx, dy in dirs.values():
                xx, yy = x + dx, y + dy
                if (xx, yy) not in flipped:
                    whites.add((xx, yy))
        
        for x, y in whites:
            neighbours = 0
            for dx, dy in dirs.values():
                if (x + dx, y + dy) in flipped:
                    neighbours += 1
            if neighbours == 2:
                to_flip.add((x, y))

        for t in to_flip:
            if t in flipped:
                flipped.remove(t)
            else:
                flipped.add(t)

        print(f'Day {day + 1}:', len(flipped))
    
if __name__ == '__main__':
    main()

