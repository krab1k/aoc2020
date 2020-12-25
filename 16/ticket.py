from collections import defaultdict

def main():
    rules = defaultdict(list)
    tickets = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                break
            name, rules_str = line.split(':')
            for rule in rules_str.split(' or '):
                low, high = rule.split('-')
                low = int(low)
                high = int(high)
                rules[name].append((low, high))
        next(f)
        your_ticket = [int(x) for x in next(f).split(',')]
        next(f)
        next(f)
        for line in f:
            line = line.strip()
            tickets.append([int(x) for x in line.split(',')])

        print(rules)

        sum_invalid = 0
        for ticket in tickets:
            print(ticket)
            for field in ticket:
                found = False
                for def_field, limits in rules.items():
                    for low, high in limits:
                        if low <= field <= high:
                            found = True
                            break
                    if found:
                        break
                if not found:
                    sum_invalid += field
        print(sum_invalid)



if __name__ == '__main__':
    main()
