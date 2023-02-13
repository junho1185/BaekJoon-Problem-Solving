from sys import stdout

n = int(input())

#upper part

for i in range(1, n+1):
    for j in range(i):
        stdout.write("*")
    for j in range((n-i)*2):
        stdout.write(" ")
    for j in range(i):
        stdout.write("*")
    print()

#lower part

for i in range(1, n+1):
    for j in range(n-i):
        stdout.write("*")
    for j in range((i)*2):
        stdout.write(" ")
    for j in range(n-i):
        stdout.write("*")
    print()