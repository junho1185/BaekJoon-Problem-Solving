from sys import stdout

n = int(input())

for i in range(n):
    for j in range(i):
        stdout.write(" ")
    for j in range((n-i)*2 - 1):
        stdout.write("*")
    print()