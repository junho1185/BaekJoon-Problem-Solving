odd_sum = 0
odd_min = 100
for i in range(7):
    n = int(input())
    if n%2 == 1:
        odd_sum += n
        if n < odd_min:
            odd_min = n
if odd_sum > 0:
    print(odd_sum)
    print(odd_min)
else:
    print(-1)