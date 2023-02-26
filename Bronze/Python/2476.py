from sys import stdin

N = int(stdin.readline())

maximum_prize = 0

for i in range(N):
    a, b, c = map(int, stdin.readline().split())
    if a == b == c:
        prize = 10000 + a*1000
    elif a == b or a == c:
        prize = 1000 + a*100
    elif b == c:
        prize = 1000 + b*100
    else:
        if a > b and a > c:
            prize = a*100
        elif b > a and b > c:
            prize = b*100
        else:
            prize = c*100
    if prize > maximum_prize:
        maximum_prize = prize

print(maximum_prize)