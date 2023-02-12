from sys import stdin

def is_sosu(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = stdin.readline()

arr = list(map(int, stdin.readline().split()))

cnt = 0

for i in arr:
    if is_sosu(i):
        cnt += 1

print(cnt)