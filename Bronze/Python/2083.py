from sys import stdin
arr = stdin.readline().split()
while arr[0] != '#':
    if int(arr[1])>17 or int(arr[2])>=80:
        print(arr[0], "Senior")
    else:
        print(arr[0], "Junior")
    arr = stdin.readline().split()