from sys import stdout

def is_creator(n):
    if n < 20:
        for i in range(1, n):
            number_list = list(map(int, str(i)))
            sum = 0
            for number in number_list:
                sum += number
            if sum + i == n:
                return True
    elif n < 100:
        for i in range(n-20, n):
            number_list = list(map(int, str(i)))
            sum = 0
            for number in number_list:
                sum += number
            if sum + i == n:
                return True
    elif n < 1000:
        for i in range(n-30, n):
            number_list = list(map(int, str(i)))
            sum = 0
            for number in number_list:
                sum += number
            if sum + i == n:
                return True
    else:
        for i in range(n-40, n):
            number_list = list(map(int, str(i)))
            sum = 0
            for number in number_list:
                sum += number
            if sum + i == n:
                return True
    return False

for i in range(1, 10000):
    if is_creator(i):
        continue
    else:
        stdout.write("%d\n"%i)