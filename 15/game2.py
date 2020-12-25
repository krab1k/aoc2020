
def main():

    appearance = {}
    with open('input.txt') as f:
        numbers = [int(x) for x in f.read().split(',')]

    print(numbers)

    for i, n in enumerate(numbers[:-1]):
        appearance[n] = i

    last = numbers[-1]
    for gen in range(len(numbers), 30000000):
        pos = appearance.get(last, None)
        if pos is None:
            appearance[last] = gen - 1
            last = 0
        else:
            appearance[last] = gen - 1
            last = gen - pos - 1

    print(last)
    

if __name__ == '__main__':
    main()
