from sys import stdin
A,B = map(int, stdin.readline().split())
C = int(stdin.readline())

if A+B >= 2*C:
    print((A+B)-2*C)
else:
    print(A+B)