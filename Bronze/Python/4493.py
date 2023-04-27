from sys import stdin

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())

    player1, player2 = 0, 0

    for j in range(n):
        p1, p2 = map(str, stdin.readline().strip().split())

        if p1 == 'R':
            if p2 == 'S':
                player1 += 1
            elif p2 == 'P':
                player2 += 1
        elif p1 == 'S':
            if p2 == 'P':
                player1 += 1
            elif p2 == 'R':
                player2 += 1
        else:
            if p2 == 'R':
                player1 += 1
            elif p2 == 'S':
                player2 += 1
    
    if player1 > player2:
        print('Player 1')
    elif player1 < player2:
        print('Player 2')
    else:
        print('TIE')