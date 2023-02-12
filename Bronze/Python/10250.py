from sys import stdin, stdout

n = int(stdin.readline())

for i in range(n):
    H, W, N = map(int, stdin.readline().split())

    if N%H == 0:
        yy = H
        xx = N//H
    else:
        yy = N%H
        xx = N//H + 1
    stdout.write("%d%02d\n"%(yy, xx))