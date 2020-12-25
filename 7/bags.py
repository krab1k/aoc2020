def check(bag, sought, bags):
    for contents in bags[bag]:
        if contents == sought:
            return True
        if check(contents, sought, bags):
            return True

    return False

def main():
    sought = 'shiny gold'

    bags = {}

    with open('input.txt') as f:
        for line in f:
            outer, inner = line.strip().split(' contain ')
            outer = ' '.join(outer.split()[:-1])
            if inner == 'no other bags.':
                bags[outer] = []
                continue

            contents = []
            for contents_str in inner.split(', '):
                c = ' '.join(contents_str.split(' ')[1:3])
                contents.append(c)

            bags[outer] = contents

    total = 0
    for bag in bags:
        if check(bag, sought, bags):
            total += 1

    print(total)

if __name__ == '__main__':
    main()
