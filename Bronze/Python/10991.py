from sys import stdout

n = int(input())

for i in range(1, n+1):
    if i == 1:
        for j in range(n-1):
            stdout.write(" ")
        stdout.write("*")
    elif i == n:
        for j in range(n):
            stdout.write("* ")
    else:
        for j in range(n-i):
            stdout.write(" ")
        for j in range(i):
            stdout.write("* ")
    print()