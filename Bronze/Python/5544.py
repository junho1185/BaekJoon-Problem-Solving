from sys import stdin
second = 0
for i in range(4):
    second += int(stdin.readline())
print(second//60)
print(second%60)