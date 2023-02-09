import math
R, C, N = map(int, input().split())

cnt = math.ceil(R/N) * math.ceil(C/N)
print(int(cnt))