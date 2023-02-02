a, b = map(int, input().split())
b /= 100
defense = a - a*b
if(defense>=100):
    print("0")
else:
    print("1")