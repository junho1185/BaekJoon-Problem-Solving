n = int(input())

if n%2 == 0:
    pieces = (n//2 + 1)**2
else:
    if n == 1:
        pieces = 2
    else:
        pieces = ((n+1)//2 + 1)*((n+1)//2)

print(pieces)