from sys import stdout

n = int(input())

#upper part

for i in range(1, n):
    for j in range(i):
        stdout.write("*")
    for j in range((n-i-1)*2 + 1):
        stdout.write(" ")
    for j in range(i):
        stdout.write("*")
    print()

#middle part

for i in range(2*n - 1):
    stdout.write("*")
print()

