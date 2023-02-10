from sys import stdin

people = list(map(int, stdin.readline().split()))

x,y,r = map(int, stdin.readline().split())

if people.count(x) == 0:
    print(0)
else:
    print(people.index(x) + 1)