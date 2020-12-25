def main():
    with open('input.txt') as f:
        time = int(f.readline())
        buses = [int(bus_id) for bus_id in f.readline().split(',') if bus_id != 'x']

    min_delay = max(buses)
    best_bus = None
    for bus in buses:
        if time % bus == 0:
            best_bus = bus
            min_delay = 0
            break
            
        if ((time // bus) + 1) * bus - time  < min_delay:
            min_delay = ((time // bus) + 1) * bus - time
            best_bus = bus

    print(best_bus * min_delay)


if __name__ == '__main__':
    main()
