from sys import stdin

n = int(stdin.readline())

for i in range(n):
    t = int(stdin.readline())
    print("Pairs for %d:" % t, end='')
    pair_cnt = 0
    for j in range(1, t//2 + 1):
        for k in range(j+1, t+1):
            if j + k == t:
                if pair_cnt:
                    print(", %d %d" % (j, k), end='')
                else:
                    print(" %d %d" % (j, k), end='')
                    pair_cnt += 1
    print()
    