from sys import stdin
a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
d = int(stdin.readline())
e = int(stdin.readline())

time = 0
if a < 0:
    time += c*(-a)  #heating up til 0
    time += d       #defreezing
    time += e*(b)
else:
    time += e*(b-a)
print(time)