from sys import stdin

n = int(stdin.readline())
scores = list(map(int, stdin.readline().split()))
streak = 0
result = 0
for score in scores:
    if score == 1:
        result += score + streak
        streak += 1
    else:
        streak = 0
print(result)