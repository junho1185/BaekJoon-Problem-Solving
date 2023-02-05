scores = []
for i in range(5):
    scores.append(int(input()))
sum = 0
for i in scores:
    if(i<40):
        sum += 40
    else:
        sum += i
print(sum//len(scores))