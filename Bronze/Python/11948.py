from sys import stdin
science = []
for i in range(4):
    science.append(int(stdin.readline()))
social = []
for i in range(2):
    social.append(int(stdin.readline()))
science.sort(reverse=True)
social.sort(reverse=True)
sum = 0
for i in science[:3]:
    sum += i
sum += social[0]
print(sum)