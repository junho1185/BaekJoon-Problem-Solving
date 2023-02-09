from sys import stdin

sum = 0

money = int(stdin.readline())
while(money != -1):
    sum += money
    money = int(stdin.readline())
print(sum)