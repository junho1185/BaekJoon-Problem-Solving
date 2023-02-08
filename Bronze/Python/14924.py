from sys import stdin
S, T, D = map(int, stdin.readline().split())

h = D//(S*2)

fly = h*T

print(fly)