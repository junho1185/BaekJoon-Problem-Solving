import sys

def get_ints():
    return list(map(int, sys.stdin.readline().split()))

list = get_ints()

list.sort()

for i in list:
    print(i, end=' ')