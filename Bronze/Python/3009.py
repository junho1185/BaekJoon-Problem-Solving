from sys import stdin

x_coordinate = []
y_coordinate = []

for i in range(3):
    x,y = map(int, stdin.readline().split())
    x_coordinate.append(x)
    y_coordinate.append(y)

for i in x_coordinate:
    if x_coordinate.count(i) == 1:
        x = i
        break

for i in y_coordinate:
    if y_coordinate.count(i) == 1:
        y = i
        break
print(x, y)