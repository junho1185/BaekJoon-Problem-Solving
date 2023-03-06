from sys import stdin

n = int(stdin.readline())

for i in range(n):
    money = 0
    s = int(stdin.readline())
    o = int(stdin.readline())
    for j in range(o):
        p, q = map(int, stdin.readline().split())
        money += p*q
    money += s
    print(money)