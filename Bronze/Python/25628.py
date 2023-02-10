bread, patty = map(int, input().split())

if bread >= patty*2:
    print(patty)
else:
    print(bread//2)