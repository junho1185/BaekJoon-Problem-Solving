from sys import stdin
N, M, K = map(int, stdin.readline().split())

number = N - (abs(M-K))

print(number)