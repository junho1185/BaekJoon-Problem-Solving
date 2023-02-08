n = int(input())
if n==1010:
    a = 10
    b = 10
elif n > 110:
    a = n//100
    b = n%100
else:
    a = n//10
    b = n%10
print(a+b)