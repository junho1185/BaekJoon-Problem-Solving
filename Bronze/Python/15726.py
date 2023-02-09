from sys import stdin
a,b,c = map(int, stdin.readline().split())
result1 = (a*b)/c
result2 = (a/b)*c

if(result1 > result2):
    print(int(result1))
else:
    print(int(result2))