from collections import deque

def main():
    player1 = deque()
    player2 = deque()
    with open('input.txt') as f:
        second = False
        for line in f:
            if line.startswith('Player'):
                continue
            if not line.strip():
                second = True
                continue
            if second:
                player2.append(int(line.strip()))
            else:
                player1.append(int(line.strip()))

    while player1 and player2:
        x = player1.popleft()
        y = player2.popleft()
        if x > y:
            player1.extend([x, y])
        else:
            player2.extend([y, x])

        print(player1)
        print(player2)

    winner = player1 if player1 else player2
    winner.reverse()
    print(sum(i * x for i, x in enumerate(winner, 1)))


if __name__ == '__main__':
    main()
