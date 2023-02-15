from sys import stdin

n = int(stdin.readline())
agree = 0
disagree = 0

for i in range(n):
    opinion = int(stdin.readline())
    if opinion == 0:
        disagree += 1
    else:
        agree += 1

if disagree > agree:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")