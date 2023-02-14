from sys import stdin

a, b = map(int, stdin.readline().split())
while a!=0:
    if a < b and b%a == 0:
        print("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")
    a, b = map(int, stdin.readline().split())