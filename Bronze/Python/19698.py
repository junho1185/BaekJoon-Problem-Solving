from sys import stdin
N,W,H,L = map(int, stdin.readline().split())

cnt = (W//L) * (H//L)

if cnt > N:
    print(N)
else:
    print(cnt)