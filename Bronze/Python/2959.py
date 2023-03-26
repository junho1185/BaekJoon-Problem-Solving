from sys import stdin

lines = list(map(int, stdin.readline().split()))

height = min(lines)

lines.remove(height)

width = max(lines)

lines.remove(width)

width = width - (width-max(lines))

print(width*height)