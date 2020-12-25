def run(instructions):
    acc = 0
    i = 0
    processed = set()
    while i < len(instructions):
        if i in processed:
            return None
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
    modify = []
    with open('input.txt') as f:
        for lineno, line in enumerate(f):
            line = line.strip()
            op, arg = line.split()
            if op == 'jmp' or op == 'nop':
                modify.append(lineno)

            arg = int(arg)
            instructions.append((op, arg))

    for lineno in modify:
        modified_instructions = list(instructions)
        if instructions[lineno][0] == 'jmp':
            modified_instructions[lineno] = ('nop', instructions[lineno][1])
        else:
            modified_instructions[lineno] = ('jmp', instructions[lineno][1])

        res = run(modified_instructions)
        if res is not None:
            print(res)
