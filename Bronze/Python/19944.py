from sys import stdin
N, M = map(int, stdin.readline().split())
if M <= 2:
    print("NEWBIE!")
elif 2 < M <= N:
    print("OLDBIE!")
else:
    print("TLE!")