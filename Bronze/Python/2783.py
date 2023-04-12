from sys import stdin

X, Y = map(int, stdin.readline().split())

minimum_price = (X/Y)*1000

n = int(stdin.readline())

for i in range(n):
    X, Y = map(int, stdin.readline().split())
    price = (X/Y)*1000
    if price < minimum_price:
        minimum_price = price

print("%.2f" % minimum_price)