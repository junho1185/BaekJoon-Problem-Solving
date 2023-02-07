from sys import stdin
A, B = map(int, stdin.readline().split())
C, D = map(int, stdin.readline().split())

times = []
times.append(A + D)
times.append(B + C)
print(min(times))