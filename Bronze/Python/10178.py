from sys import stdin

n = int(stdin.readline())

for i in range(n):
    c,v = map(int, stdin.readline().split())

    print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')