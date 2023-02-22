from sys import stdin

n = int(stdin.readline())

for i in range(n):
    r,e,c = map(int, stdin.readline().split())

    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")