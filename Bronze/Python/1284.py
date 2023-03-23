from sys import stdin

n = int(stdin.readline())

while n != 0:
    space = 0
    while n > 0:
        if n%10 == 0:
            space += 5
        elif n%10 == 1:
            space += 3
        else:
            space += 4
        n = n//10
    space += 1
    print(space)
    n = int(stdin.readline())