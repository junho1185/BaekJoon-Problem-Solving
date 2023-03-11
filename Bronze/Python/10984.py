from sys import stdin

T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    credit = 0
<<<<<<< HEAD
    grades = 0
    
    for j in range(N):
        c, g = map(float, stdin.readline().split())

        credit += c
        grades += g*c

    print("%d %.1f"%(credit, grades/credit))
=======
    gpa = 0
    for j in range(N):
        c, g = map(float, stdin.readline().split())
        credit += c
        gpa += g/c
    gpa /= N

    print("%d %.1f"%(credit, gpa))
>>>>>>> f495920 (0311 commit)
