from sys import stdin

a,b,c = map(int, stdin.readline().split())

while a > 0 or b > 0 or c > 0:
    len_list = []
    len_list.append(a)
    len_list.append(b)
    len_list.append(c)
    max_len = max(len_list)
    sum = 0
    
    for i in len_list:
        sum += i
    
    if max_len >= (sum-max_len):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")
    a,b,c = map(int, stdin.readline().split())
