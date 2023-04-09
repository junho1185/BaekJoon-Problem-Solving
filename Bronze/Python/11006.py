from sys import stdin

n = int(stdin.readline())

for i in range(n):
    legs, chickens = map(int, stdin.readline().split())

    print((chickens*2 - legs), chickens - (chickens*2 - legs))