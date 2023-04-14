n = int(input())

cnt = 0

for i in range(1, n+1):
    number = str(i)
    cnt += number.count('3') + number.count('6') + number.count('9')
print(cnt)