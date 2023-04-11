from sys import stdin

n = int(stdin.readline())

for i in range(n):
    A, B, C, D, E = map(int, stdin.readline().split())

    sum = 350.34 * A + 230.9 * B + 190.55 * C + 125.3 * D + 180.9 * E

    print("$%.2f" % sum)