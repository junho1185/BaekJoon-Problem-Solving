from sys import stdin

T = int(stdin.readline())

for i in range(T):
    nums = list(map(int, stdin.readline().split()))

    print(sum(nums))