total = 0
questions = set()
with open('input.txt') as f:
    for line in f:
        if not line.strip():
            total += len(questions)
            questions = set()
        else:
            questions |= set(line.strip())

total += len(questions)
print(total)
