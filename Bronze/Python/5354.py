from sys import stdin

def printJBox(size):
    for i in range(size):
        if i == 0 or i == size-1:
            for j in range(size):
                print('#', end='')
            print()
        else:
            print('#', end='')
            for j in range(size-2):
                print('J', end='')
            print('#')
    print()

n = int(stdin.readline())

for i in range(n):
    size = int(stdin.readline())
    printJBox(size)