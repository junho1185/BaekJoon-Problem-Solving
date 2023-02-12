from sys import stdin, stdout

n = int(stdin.readline())

for i in range(n):
    for j in range(i):
        stdout.write(" ")
    for j in range(n-i):
        stdout.write("*")
    stdout.write("\n")