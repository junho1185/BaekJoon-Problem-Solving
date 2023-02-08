n = int(input())
n -= 1
n = n % 8
n += 1
if n > 5:
    n = 5 + (5-n)
print(n)