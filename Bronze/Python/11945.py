from sys import stdin
N, M = map(int, stdin.readline().split())
fish_bread = []
for i in range(N):
    fish_bread.append(stdin.readline().strip())
for i in range(N):
    length = len(fish_bread[i])
    for j in range(length):
        print(fish_bread[i][length-j-1], end='')
    print()
