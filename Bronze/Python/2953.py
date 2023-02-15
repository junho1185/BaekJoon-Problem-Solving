scores = []
sums = []
for i in range(5):
    score = list(map(int, input().split()))
    scores.append(score)

for i in range(5):
    sum = 0
    for j in scores[i]:
        sum += j
    sums.append(sum)

print(sums.index(max(sums)) + 1, max(sums))