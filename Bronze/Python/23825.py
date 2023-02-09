N, M = map(int, input().split())

N = N//2
M = M//2

if N < M:
    print(N)
else:
    print(M)