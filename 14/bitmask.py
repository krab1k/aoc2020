def apply_mask(value, mask):
    one_mask = mask.replace('X', '1')
    zero_mask = mask.replace('X', '0')
    return (int(one_mask, 2) & value) | int(zero_mask, 2)


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
            memory[command[1]] = apply_mask(command[2], current_mask)

    print(sum(memory.values()))

if __name__ == '__main__':
    main()


