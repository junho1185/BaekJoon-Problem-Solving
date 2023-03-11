from sys import stdin

N, M = map(int, stdin.readline().split())

baskets = [0 for i in range(N)]

for i in range(M):
    a, b, c = map(int, stdin.readline().split())

    for j in range(a-1, b):
        baskets[j] = c
    
for basket in baskets:
    print(basket, end = ' ')