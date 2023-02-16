from sys import stdout

n = int(input())

for i in range(n-1):
    stdout.write(" ")
stdout.write("*\n")

for i in range(2, n):
    for j in range(n-i):
        stdout.write(" ")
    stdout.write("*")
    for j in range((i-1)*2 -1):
        stdout.write(" ")
    stdout.write("*\n")

if n!=1:
    for i in range(n*2 - 1):
        stdout.write("*")