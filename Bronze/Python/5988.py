from sys import stdin

n = int(stdin.readline())

for i in range(n):
    number = int(stdin.readline())

    if number % 2 == 0:
        print('even')
    else:
        print('odd')