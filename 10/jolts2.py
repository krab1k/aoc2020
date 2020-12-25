
def possible(data):
    cache = {max(data) : 1}
    
    for i in range(len(data) - 2, -1, -1):
        s = 0
        if i + 1 < len(data) and data[i + 1] - data[i] <= 3:
            s += cache[data[i + 1]]

        if i + 2 < len(data) and data[i + 2] - data[i] <= 3:
            s += cache[data[i + 2]]

        if i + 3 < len(data) and data[i + 3] - data[i] <= 3:
            s += cache[data[i + 3]]

        cache[data[i]] = s

    return cache.get(1, 0) + cache.get(2, 0) + cache.get(3, 0) 



def main():
    data = []
    with open('input.txt') as f:
        for line in f:
            data.append(int(line.strip()))

    data.sort()
    res = possible(data)
    print(res)

if __name__ == '__main__':
    main()

