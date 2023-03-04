from sys import stdin

T = int(stdin.readline())

for i in range(T):
    y_sum = 0 
    k_sum = 0
    for j in range(9):
        yonsei, korea = map(int, stdin.readline().split())
        y_sum += yonsei
        k_sum += korea
    if y_sum > k_sum:
        print("Yonsei")
    elif y_sum < k_sum:
        print("Korea")
    else:
        print("Draw")
