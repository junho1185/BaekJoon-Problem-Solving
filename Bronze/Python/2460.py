on_board = 0
maximum_on_board = 0
for i in range(10):
    off, on = map(int, input().split())
    on_board -= off
    on_board += on

    if on_board > maximum_on_board:
        maximum_on_board = on_board
print(maximum_on_board)