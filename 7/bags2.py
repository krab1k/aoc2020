def sum_bags(bag, bags):
    return sum(cc + cc * sum_bags(ct, bags) for ct, cc in bags[bag])


def main():
    first = 'shiny gold'

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
                ct = ' '.join(contents_str.split(' ')[1:3])
                cc = int(contents_str.split(' ')[0])
                contents.append((ct, cc))

            bags[outer] = contents

    print(sum_bags(first, bags))

if __name__ == '__main__':
    main()
