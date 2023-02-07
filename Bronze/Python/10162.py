import sys

t = int(sys.stdin.readline())

five_m = 0
one_m = 0
ten_s = 0

if t%10 != 0:
    print(-1)
else:
    while t > five_m * 300:
        five_m += 1
    if t < five_m * 300:
        five_m -= 1
    while t > five_m * 300 + one_m * 60:
        one_m += 1
    if t < five_m * 300 + one_m * 60:
        one_m -= 1
    while t > five_m * 300 + one_m * 60 + ten_s * 10:
        ten_s += 1
    if t < five_m * 300 + one_m * 60 + ten_s * 10:
        ten_s -= 1
    print(five_m, one_m, ten_s)