import string

req = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

good = 0
with open('input.txt') as f:
    record = {'_validity': True}
    for line in f:
        if not line.strip():
            if set(record) | {'cid'} == req | {'_validity'} and record['_validity']:
                good += 1
            record = {'_validity': True}
        else:
            entries = line.strip().split(' ')
            for e in entries:
                k, v = e.split(':')
                if k == 'byr':
                    v = int(v)
                    if v < 1920 or v > 2002:
                        print('bad byr: ', v)
                        record['_validity'] = False
                        break
                if k == 'iyr':
                    v = int(v)
                    if v < 2010 or v > 2020:
                        print('bad iyr: ', v)
                        record['_validity'] = False
                        break
                if k == 'eyr':
                    v = int(v)
                    if v < 2020 or v > 2030:
                        print('bad eyr: ', v)
                        record['_validity'] = False
                        break
                if k == 'hgt':
                    try:
                        unit = v[-2:]
                        h = int(v[:-2])
                    except:
                        print('bad hgt: ', v)
                        record['_validity'] = False
                        break
                    if unit == 'cm':
                        if h < 150 or h > 193:
                            print('bad hgt: ', v)
                            record['_validity'] = False
                            break
                    elif unit == 'in':
                        if h < 59 or h > 76:
                            print('bad hgt: ', v)
                            record['_validity'] = False
                            break
                if k == 'hcl':
                    if v[0] != '#' or set(v[1:]) > set(string.hexdigits.lower()):
                        print('bad hcl: ', v)
                        record['_validity'] = False
                        break

                if k == 'ecl':
                    if v not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                        print('bad ecl: ', v)
                        record['_validity'] = False
                        break

                if k == 'pid':
                    if len(v) != 9 or set(v) > set(string.digits):
                        print('bad pid: ', v)
                        record['_validity'] = False
                        break

                record[k] = v

    if set(record) | {'cid'} == req | {'_validity'} and record['_validity']:
        good += 1

print(good)

