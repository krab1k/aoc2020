from collections import Counter

data = []

good = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        req, password = line.split(':')
        req, c = req.split(' ')
        low, high = req.split('-')
        password = password.strip()

        c1 = password[int(low) - 1]
        c2 = password[int(high) - 1]
        if c1 != c2 and c in {c1, c2}:
            good += 1

print(good)
