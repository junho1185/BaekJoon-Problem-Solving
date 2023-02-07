from sys import stdin
A, B = map(int, stdin.readline().split())
M = (B-A)/400
print(1/(1+10**M))