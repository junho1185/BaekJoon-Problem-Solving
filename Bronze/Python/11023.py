from sys import stdin

numbers = list(map(int, stdin.readline().split()))

sum = 0

for number in numbers:
    sum += number

print(sum)