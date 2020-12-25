from collections import Counter

data = []

good = 0
with open('input.txt') as f:
    for line in f:
        req, password = line.strip().split(':')
        req, c = req.split(' ')
        low, high = req.split('-')
        
        if int(low) <= password.count(c) <= int(high):
            good += 1

print(good)
