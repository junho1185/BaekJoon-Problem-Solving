from sys import stdin
L = int(stdin.readline())
A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())
D = int(stdin.readline())

if A//C > B//D:
    L -= A//C
    if A%C != 0:
        L -= 1
else:
    L -= B//D
    if B%D != 0:
        L -= 1

print(L)