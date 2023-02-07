from sys import stdin
k, n, m = map(int, stdin.readline().split())
mom_money = n*k - m
if mom_money < 0:
    mom_money = 0
print(mom_money)