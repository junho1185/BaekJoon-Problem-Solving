from sys import stdin

yes = "DA"
no = "NE"

N, W, H = map(int, stdin.readline().split())

diagonal = (W**2 + H**2)**(1/2)

for i in range(N):
    length = int(stdin.readline())

    if length <= W or length <= H or length <= diagonal:
        print(yes)
    else:
        print(no)