a, b = map(int, input().split())

if a%4 == 0:
    ax = a//4
    ay = 4
else:
    ax = a//4 + 1
    ay = a%4

if b%4 == 0:
    bx = b//4
    by = 4
else:
    bx = b//4 + 1
    by = b%4

x_move = abs(bx - ax)
y_move = abs(by - ay)

print(x_move + y_move)