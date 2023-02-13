from sys import stdout

n = int(input())

for i in range(n):
    for j in range(i+1):
        stdout.write("*")
    print()

for i in range(1, n):
    for j in range(n-i):
        stdout.write("*")
    print()