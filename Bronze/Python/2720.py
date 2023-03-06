from sys import stdin

n = int(stdin.readline())

for i in range(n):
    change = int(stdin.readline())
    current_change = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    while quarter*25 <= change:
        quarter += 1
    quarter -= 1
    current_change += quarter*25

    while current_change + dime*10 <= change:
        dime += 1
    dime -= 1
    current_change += dime*10

    while current_change + nickel*5 <= change:
        nickel += 1
    nickel -= 1
    current_change += nickel*5

    while current_change + penny <= change:
        penny += 1
    penny -= 1
    current_change += penny

    print(quarter, dime, nickel, penny)