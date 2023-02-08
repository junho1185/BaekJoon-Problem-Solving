from sys import stdin
skills = list(map(int, stdin.readline().split()))
print(abs((skills[0]+skills[3])-(skills[1]+skills[2])))