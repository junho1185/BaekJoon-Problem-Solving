from sys import stdin

n = int(stdin.readline())

tmp_num = int(stdin.readline())

while(tmp_num != 0):
    if tmp_num % n == 0:
        print(f'{tmp_num} is a multiple of {n}.')
    else:
        print(f'{tmp_num} is NOT a multiple of {n}.')
    tmp_num = int(stdin.readline())