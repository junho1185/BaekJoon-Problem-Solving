from sys import stdin

fx = stdin.readline().strip()
prev_num = int(fx)
tmp = 0
for i in range(len(fx)):
    number = int(fx[0])*len(fx)
    fx = str(number)
    if prev_num == number:
        print("FA")
        tmp = 1
        break

    prev_num = number
if tmp == 0:
    print("NFA")