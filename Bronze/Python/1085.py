x,y,w,h = map(int, input().split())

minimum = x

if y < minimum:
    minimum = y
if w-x < minimum:
    minimum = w-x
if h-y < minimum:
    minimum = h-y
print(minimum)