import sys

arr = [0 for i in range(26)]

word = sys.stdin.readline().strip()

for i in word:
    arr[ord(i) - ord('a')] += 1

for i in arr:
    print(i, end=' ')