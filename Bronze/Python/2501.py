a, k = map(int, input().split())
dividers = []

for i in range(1, a+1):
    if a%i == 0:
        dividers.append(i)
        if len(dividers) >= k:
            break

if len(dividers) < k:
    print(0)
else:
    print(dividers[k-1])