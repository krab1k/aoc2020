from collections import deque


def game(player1, player2):
    print('Running new (sub)game')
  
    prev_states = set()
    
    winner_no = None
    round = 1
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in prev_states:
            print('Avoiding cycle, player 1 wins.')
            return player1, 1
        else:
            prev_states.add(state)

        x = player1.popleft()
        y = player2.popleft()
        print('Round: ', round)
        print('Dealing: ', x, y)
        if x <= len(player1) and y <= len(player2):
            deck1 = deque(list(player1)[:x])
            deck2 = deque(list(player2)[:y])
            _, sub_winner = game(deck1, deck2)
            print('Back to previous game')
            if sub_winner == 1:
                player1.extend([x, y])
            else:
                player2.extend([y, x])
        else:
            if x > y:
                player1.extend([x, y])
            else:
                player2.extend([y, x])

        print('Player1: ', player1)
        print('Player2: ', player2)
        round += 1
    if player1:
        return player1, 1
    else:
        return player2, 2


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


    winner, _ = game(player1, player2)
    winner.reverse()
    print(sum(i * x for i, x in enumerate(winner, 1)))


if __name__ == '__main__':
    main()
