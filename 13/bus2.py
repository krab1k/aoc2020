
def main():
    with open('input.txt') as f:
        f.readline()
        buses = [(offset, int(bus_id)) for offset, bus_id in enumerate(f.readline().split(',')) if bus_id != 'x']

    time = 0
    increment = 1
    for offset, bus in buses:
        while (time + offset) % bus != 0:
            time += increment
        increment *= bus

    print(time)
            

if __name__ == '__main__':
    main()
