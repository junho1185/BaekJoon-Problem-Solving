from sys import stdin

arr = []
max_i = 1
max_j = 1
max_num = 0
for i in range(9):
    tmp_arr = list(map(int, stdin.readline().split()))
    arr.append(tmp_arr)

    if max(tmp_arr) > max_num:
        max_i = i + 1
        max_j = tmp_arr.index(max(tmp_arr)) + 1
        max_num = max(tmp_arr)

print(max_num)
print(max_i, max_j)
