from sys import stdin

year, month, day = map(int, stdin.readline().split())
now_y, now_m, now_d = map(int, stdin.readline().split())

age = now_y - year
if month == now_m and day > now_d:
    age -= 1
elif month > now_m:
    age -= 1
print(age)
print(now_y - year + 1)
print(now_y - year)