from sys import stdin

for i in range(3):
    yoots = list(map(int, stdin.readline().split()))
    sum = 0
    for yoot in yoots:
        sum += yoot
    if sum == 0:
        print("D")
    elif sum == 1:
        print("C")
    elif sum == 2:
        print("B")
    elif sum == 3:
        print("A")
    elif sum == 4:
        print("E")