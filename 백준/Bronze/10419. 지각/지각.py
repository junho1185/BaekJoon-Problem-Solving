from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    d = int(stdin.readline())
    t = 1
    while(t + t*t <= d):
        t += 1
    print(t-1)