from sys import stdin

n = int(stdin.readline())

for i in range(n):
    numbers = list(map(int, stdin.readline().split()))
    sum = 0
    min_even = 100

    for number in numbers:
        if number % 2 == 0:
            sum += number
            
            if number < min_even:
                min_even = number

    print(sum, min_even)