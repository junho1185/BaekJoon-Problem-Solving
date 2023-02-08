from sys import stdin
sum, diff = map(int, stdin.readline().split())

if sum < diff:
    print(-1)
elif sum == diff:
    print(sum, 0)
elif sum%2 == 0:
    if diff == 0:
        print(sum//2, sum//2)
    elif diff%2 == 1:
        print(-1)
    else:
        print(sum//2 + diff//2, sum//2 - diff//2)
else:
    if diff == 0:
        print(-1)
    elif diff%2 == 0:
        print(-1)
    else:
        print((sum//2 + diff//2 + 1), sum//2 - diff//2)