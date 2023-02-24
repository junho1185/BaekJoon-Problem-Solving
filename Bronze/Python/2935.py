a = input().strip()
op = input().strip()
b = input().strip()

if op == '+':
    print(int(a) + int(b))
else:
    print(1, end='')
    for i in range(len(a) + len(b) -2):
        print(0, end='')