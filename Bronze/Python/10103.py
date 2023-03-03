from sys import stdin

n = int(stdin.readline())

changyoung = 100
sangduk = 100

for i in range(n):
    c_dice, s_dice = map(int, stdin.readline().split())
    if c_dice > s_dice:
        sangduk -= c_dice
    elif c_dice < s_dice:
        changyoung -= s_dice
    
print(changyoung)
print(sangduk)