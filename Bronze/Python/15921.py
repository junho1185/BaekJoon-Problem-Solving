from sys import stdin

n = int(stdin.readline())

if n == 0:
    print("divide by zero")
    exit()

arr = list(map(int, stdin.readline().split()))
sum = 0

for i in arr:
    sum += i

avg = sum/n
expectation = 0

for i in arr:
    expectation += i*(1/n)

print("%.2f"%(avg/expectation))