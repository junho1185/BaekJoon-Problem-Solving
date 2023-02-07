from sys import stdin
A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

if A+B+C == 180:
    if A==B==C:
        print("Equilateral")
    elif A==B or A==C or B==C:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")