from sys import stdin

n = int(stdin.readline())

cups = [1, 2, 3]

for i in range(n):
    a, b = map(int, stdin.readline().split())
    a -= 1
    b -= 1

    tmp = cups[a]
    cups[a] = cups[b]
    cups[b] = tmp
print(cups.index(1) + 1)