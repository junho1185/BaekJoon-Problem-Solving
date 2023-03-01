from sys import stdin

n = int(stdin.readline())

for i in range(n):
    tmp_number = int(stdin.readline())
    number_list = list(map(int, stdin.readline().split()))
    sum = 0
    for number in number_list:
        sum += number
    print(sum)
    number_list.clear()
