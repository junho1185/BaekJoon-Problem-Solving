from sys import stdin

max_on_board = 0
on_board = 0
for i in range(4):
    off, on = map(int, stdin.readline().split())
    on_board -= off
    on_board += on
    if on_board > max_on_board:
        max_on_board = on_board
print(max_on_board)