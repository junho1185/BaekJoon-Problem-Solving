from sys import stdin
n = int(stdin.readline())
for i in range(1, n+1):
    str = stdin.readline().strip()
    print('%d. %s'%(i, str))