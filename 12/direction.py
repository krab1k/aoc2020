def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            comm, arg = line[0], int(line[1:])
            data.append((comm, arg))

    x = 0
    y = 0
    d = 90
    for comm, arg in data:
        if comm == 'N':
            y -= arg
        elif comm == 'S':
            y += arg
        elif comm == 'W':
            x -= arg
        elif comm == 'E':
            x += arg
        elif comm == 'L':
            d = (d - arg) % 360
        elif comm == 'R':
            d = (d + arg) % 360
        elif comm == 'F':
            if d == 90:
                x += arg
            elif d == 180:
                y += arg
            elif d == 270:
                x -= arg
            elif d == 0:
                y -= arg
            else:
                raise RuntimeError('Invalid angle')

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
