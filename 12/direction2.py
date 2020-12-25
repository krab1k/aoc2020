def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            comm, arg = line[0], int(line[1:])
            data.append((comm, arg))

    x = 0
    y = 0

    wx = 10
    wy = -1
    
    for comm, arg in data:
        if comm == 'N':
            wy -= arg
        elif comm == 'S':
            wy += arg
        elif comm == 'W':
            wx -= arg
        elif comm == 'E':
            wx += arg
        elif comm == 'L':
            if arg == 90:
                wx, wy = wy, -wx
            elif arg == 180:
                wx, wy = -wx, -wy
            elif arg == 270:
                wx, wy = -wy, wx
            else:
                raise RuntimeError('Wrong angle')
        elif comm == 'R':
            if arg == 90:
                wx, wy = -wy, wx
            elif arg == 180:
                wx, wy = -wx, -wy
            elif arg == 270:
                wx, wy = wy, -wx
            else:
                raise RuntimeError('Wrong angle')

        elif comm == 'F':
            x += arg * wx
            y += arg * wy
        
    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
