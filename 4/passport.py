req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

good = 0
with open('input.txt') as f:
    record = {}
    for line in f:
        if not line.strip():
            if set(record) | {'cid'} == req:
                print(record)
                good += 1
            record = {}
        else:
            entries = line.strip().split(' ')
            for e in entries:
                k, v = e.split(':')
                record[k] = v
    if set(record) | {'cid'} == req:
        print(record)
        good += 1

print(good)

