from sys import stdout

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        stdout.write(' ')
    for j in range(i*2 + 1):
        stdout.write('*')
    stdout.write('\n')