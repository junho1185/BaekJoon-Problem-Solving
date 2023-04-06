from sys import stdin

n = int(stdin.readline())

for i in range(n):
    price = float(stdin.readline())
    print(f'$%.2f' % (0.8*price))