from sys import stdin

n = int(stdin.readline())
cnt = 0
milk = 0

milk_shop_list = list(map(int, stdin.readline().split()))

for milk_shop in milk_shop_list:
    if milk_shop == cnt:
        milk += 1
        cnt += 1
        if cnt > 2:
            cnt = 0
    elif milk_shop == 0 and milk == 0:
        milk += 1
        cnt = 0

print(milk)