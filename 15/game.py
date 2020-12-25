
def main():
    said = []
    with open('input.txt') as f:
        numbers = [int(x) for x in f.read().split(',')]

    print(numbers)

    for i in numbers:
        said.append(i)

    for gen in range(2020 - len(numbers)):
        last = said[-1]
        i = len(said) - 2
        while i >= 0 and said[i] != last:
            i -= 1
        if i == -1:
            said.append(0)
        else:
            said.append(len(said) - 1 - i)

    print(said[-1])

if __name__ == '__main__':
    main()
