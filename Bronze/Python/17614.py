n = int(input())

cnt = 0

for i in range(1, n+1):
    number = i
    while number > 0:
        if number % 10 == 3 or number % 10 == 6 or number % 10 == 9:
            cnt += 1
        number = number // 10
print(cnt)