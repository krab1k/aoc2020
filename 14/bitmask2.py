import itertools


def get_addresses(address, mask):
    addresses = []
    new_mask = mask.replace('X', '0')
    address |= int(new_mask, 2)
    float_mask = mask.replace('0', '1').replace('X', '0')
    address &= int(float_mask, 2)
    positions = [i for i, x in enumerate(mask) if x == 'X']
    for bits in itertools.product(range(2), repeat=len(positions)): 
         s = 0
         for x, b in zip(positions, bits): 
             s += b * 2 ** (36 - x - 1) 
         addresses.append(address + s)

    return addresses


def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            comm, arg = line.split(' = ')
            if comm == 'mask':
                data.append(('mask', arg))
            else:
                data.append(('mem', int(comm[4:-1]), int(arg)))

    memory = {}

    current_mask = 'X' * 36
    for command in data:
        if command[0] == 'mask':
            current_mask = command[1]
        else:
            for add in get_addresses(command[1], current_mask):
                memory[add] = command[2]

    print(sum(memory.values()))

if __name__ == '__main__':
    main()

