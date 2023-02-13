from sys import stdin

def is_jikgak(a,b,c):
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return True
    else:
        return False

a,b,c = map(int, stdin.readline().split())
while a != 0:
    if is_jikgak(a,b,c):
        print("right")
    else:
        print("wrong")
    a,b,c = map(int, stdin.readline().split())