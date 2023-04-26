from sys import stdin, stdout

n = int(stdin.readline())

face = []

for i in range(n):
    face.append(stdin.readline())

condition = int(stdin.readline())

if condition == 1:
    for i in range(n):
        for j in range(n):
            stdout.write(face[i][j])
        stdout.write('\n')
elif condition == 2:
    for i in range(n):
        for j in range(n):
            stdout.write(face[i][n-j-1])
        stdout.write('\n')
else:
    for i in range(n):
        for j in range(n):
            stdout.write(face[n-i-1][j])
        stdout.write('\n')