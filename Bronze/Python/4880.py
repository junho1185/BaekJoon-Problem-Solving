from sys import stdin

while True:
    n1, n2, n3 = map(int, stdin.readline().split())

    if n1 == n2 == n3 == 0:
        break
    
    if n3 - n2 == n2 - n1:
        print("AP", n3 + (n3 - n2))
    elif n3//n2 == n2//n1:
        print("GP", n3*(n3//n2))