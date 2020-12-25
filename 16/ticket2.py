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

        valid_tickets = [your_ticket]
        for ticket in tickets:
            valid_ticket = True
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
                    valid_ticket = False
                    break
            if valid_ticket:
                valid_tickets.append(ticket)

        pos = {name: set(range(len(rules))) for name in rules}

        no_items = len(tickets[0])
        for name in rules:
            for i in range(no_items):
                for ticket in valid_tickets:
                    val = ticket[i]
                    valid = False
                    for low, high in rules[name]:
                        if low <= val <= high:
                            valid = True
                            break
                    if not valid:
                        pos[name].discard(i)
                        break
        finished = {}
        while len(finished) != no_items:
            for name, i in pos.items():
                if len(i) == 1:
                    break
            
            val = list(i)[0]
            finished[name] = val
            del pos[name]
            for name in pos:
                pos[name].discard(val)

        departures_keys = [idx for k, idx in finished.items() if k.startswith('departure')]

        mult = 1
        for key in departures_keys:
            mult *= your_ticket[key]
        print(mult)


if __name__ == '__main__':
    main()
