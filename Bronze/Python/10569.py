from sys import stdin

n = int(stdin.readline())

for i in range(n):
    v, e = map(int, stdin.readline().split())

    face = 2 - v + e

    print(face)