from sys import stdin

n = int(stdin.readline())

students = list(map(int, stdin.readline().split()))

cnt = 0

for i in range(n):
    if students[i] != i + 1:
        cnt += 1

print(cnt)