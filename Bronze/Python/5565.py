from sys import stdin

total = int(stdin.readline())
sum = 0
for i in range(9):
    price = int(stdin.readline())
    sum += price
print(total-sum)