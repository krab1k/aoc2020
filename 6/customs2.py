import string

total = 0
questions = set(string.ascii_lowercase)
with open('input.txt') as f:
    for line in f:
        if not line.strip():
            total += len(questions)
            questions = set(string.ascii_lowercase)
        else:
            questions &= set(line.strip())

total += len(questions)
print(total)
