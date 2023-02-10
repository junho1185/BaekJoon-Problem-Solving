n = int(input())
cnt = 0
for i in range(n):
    left = int(input().strip('D-'))
    if left <= 90:
        cnt += 1
print(cnt)