from sys import stdin

n = int(stdin.readline())
a,b = map(int, stdin.readline().split())
minimum = 1001
if a <= b:
    minimum = b

for i in range(n-1):
    a,b = map(int, stdin.readline().split())
    if a <= b and b < minimum:
        minimum = b

if minimum == 1001:
    print(-1)
else:
    print(minimum)