abc = list(map(int, input().split()))

seq = list(input())

abc.sort()

for i in range(3):
    print(abc[ord(seq[i]) - ord('A')], end = ' ')