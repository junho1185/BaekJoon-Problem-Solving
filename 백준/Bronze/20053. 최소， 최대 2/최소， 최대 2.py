from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))
    print(min(numbers), max(numbers))