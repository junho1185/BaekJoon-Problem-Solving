a,b,c = map(int, input().split())
row = c // b
col = c - row*b

print(row, col)