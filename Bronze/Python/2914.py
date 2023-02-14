import math

A, I = map(int, input().split())

goal = I
bribes = A*I

while math.ceil(bribes/A) == goal:
    bribes -= 1
print(bribes+1)