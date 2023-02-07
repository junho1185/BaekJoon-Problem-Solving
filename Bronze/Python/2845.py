from sys import stdin

L, P = map(int, stdin.readline().split())
news = list(map(int, stdin.readline().split()))
diff = []
for i in news:
    diff.append(i - L*P)
for i in diff:
    print(i, end=' ')