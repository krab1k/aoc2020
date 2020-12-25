def get_loop_size(pub_key):
    v = 1
    s = 7
    loop_size = 0
    while v != pub_key:
        v *= s
        v %= 20201227
        loop_size += 1

    return loop_size


def transform(s, loop_size):
    v = 1
    for i in range(loop_size):
        v *= s
        v %= 20201227

    return v


def main():
    with open('input.txt') as f:
        card_pub, door_pub = [int(x) for x in f.read().split('\n') if x]

    print(card_pub, door_pub)

    card_loop_size = get_loop_size(card_pub)
    door_loop_size = get_loop_size(door_pub)


    print(transform(card_pub, door_loop_size))
    print(transform(door_pub, card_loop_size))

if __name__ == '__main__':
    main()
