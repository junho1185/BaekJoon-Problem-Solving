from sys import stdin

numbers = list(map(int, stdin.readline().split()))

numbers.sort()

gc = numbers[1] - numbers[0]

if gc == (numbers[2] - numbers[1]):     #already right
    print(numbers[2] + gc)
elif gc > (numbers[2] - numbers[1]):
    print(numbers[0] + gc//2)
else:
    print(numbers[1] + gc)