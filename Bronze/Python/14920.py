n = int(input())
cn = 1

while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1
    cn += 1

print(cn)