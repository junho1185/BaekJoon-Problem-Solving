from sys import stdin

n = int(stdin.readline())

for i in range(n):
    hP, mP, attack, defense, a_HP, a_MP, a_Attack, a_Defense = map(int, stdin.readline().split())

    hP += a_HP
    if hP < 1:
        hP = 1
    mP += a_MP
    if mP < 1:
        mP = 1
    attack += a_Attack
    if attack < 0:
        attack = 0
    defense += a_Defense

    stat = hP + 5*mP + 2*attack + 2*defense

    print(stat)