from sys import stdout

n = int(input())

#upper part

for i in range(n-1):
    for j in range(i):
        stdout.write(" ")
    for j in range((n-i-1)*2 + 1):
        stdout.write("*")
    stdout.write('\n')

#lower part

for i in range(n):
    for j in range(n-i-1):
        stdout.write(" ")
    for j in range(i*2 + 1):
        stdout.write("*")
    stdout.write("\n")