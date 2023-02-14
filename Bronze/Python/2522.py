from sys import stdout

n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        stdout.write(" ")
    for j in range(i):
        stdout.write("*")
    print()

for i in range(1,n):
    for j in range(i):
        stdout.write(" ")
    for j in range(n-i):
        stdout.write("*")
    print()