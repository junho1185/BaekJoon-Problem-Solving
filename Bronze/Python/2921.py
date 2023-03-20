import itertools as it

n = int(input())

points = 0

for i in range(n+1):
    for j in range(i, n+1):
        points += i+j

print(points)