n = int(input())

power_of_2 = 1
flag = 0

while n >= power_of_2:
    if n == power_of_2:
        flag = 1
    power_of_2 *= 2

print(flag)
    