from collections import defaultdict
import re


def is_valid(string, rules, init):
    if string == init:
        return True

    while string and init and string[0] == init[0]:
        string = string[1:]
        init = init[1:]
    
    if not string or not init:
        return False

    for option in rules[init[0]]:
        if is_valid(string, rules, [*option, *init[1:]]):
            return True

    return False


def main():
    rules = defaultdict(list)
    terminals = {}
    strings = []
    with open('input.txt') as f:
        for line in f:
            if not line.strip():
                break
            m = re.search('(\d+):((?: \d+)+)(?: \|((?: \d+)+))?', line)
            if m is not None:
                symb = int(m.group(1))
                for rhs in m.groups()[1:]:
                    if rhs is None:
                        continue
                    rules[symb].append([int(x) for x in rhs.split()])
            else:
                m = re.search('(\d+): "(.)"', line)
                symb = int(m.group(1))
                term = m.group(2)
                terminals[term] = symb

        for line in f:
            strings.append([terminals[c] for c in line.strip()])

        s = 0
        for string in strings:
            if is_valid(string, rules, [0]):
                s += 1
        print(s)

if __name__ == '__main__':
    main()

