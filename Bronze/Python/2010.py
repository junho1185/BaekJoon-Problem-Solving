from sys import stdin

n = int(stdin.readline())

sum = 0

for i in range(n):
    holes = int(stdin.readline())
    sum += holes - 1

print(sum + 1)