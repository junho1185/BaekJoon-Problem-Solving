import sys
burgers = []
for i in range(3):
    burgers.append(int(sys.stdin.readline()))
cola = int(sys.stdin.readline())
cider = int(sys.stdin.readline())
if cola > cider:
    sum = min(burgers) + cider - 50
else:
    sum = min(burgers) + cola - 50
print(sum)