from sys import stdin

n = int(stdin.readline())

for i in range(n):
    a,b = map(int, stdin.readline().split())

    prize_money = 0

    if a > 21:
        prize_money += 0
    elif a > 15:
        prize_money += 100000   #6th place, 100,000 won
    elif a > 10:
        prize_money += 300000   #5th place, 300,000 won
    elif a > 6:
        prize_money += 500000   #4th place, 500,000 won
    elif a > 3:
        prize_money += 2000000  #3rd place, 2,000,000 won
    elif a > 1:
        prize_money += 3000000  #2nd place, 3,000,000 won
    elif a == 1:
        prize_money += 5000000  #1st place, 5,000,000 won
    else:
        prize_money += 0
    
    if b > 31:
        prize_money += 0
    elif b > 15:
        prize_money += 320000
    elif b > 7:
        prize_money += 640000
    elif b > 3:
        prize_money += 1280000
    elif b > 1:
        prize_money += 2560000
    elif b == 1:
        prize_money += 5120000
    else:
        prize_money += 0
    
    print(prize_money)