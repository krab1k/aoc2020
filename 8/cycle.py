def run(instructions):
    acc = 0
    i = 0
    processed = set()
    while i not in processed:
        processed.add(i)
        op, arg = instructions[i]
        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += arg
            i += 1
        else:
            i += arg

    return acc

if __name__ == '__main__':
    instructions = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            op, arg = line.split()
            arg = int(arg)
            instructions.append((op, arg))


    print(run(instructions))
