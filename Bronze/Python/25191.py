N = int(input())
cola, beer = map(int, input().split())

max_cnt = cola//2 + beer

if max_cnt > N:
    print(N)
else:
    print(max_cnt)