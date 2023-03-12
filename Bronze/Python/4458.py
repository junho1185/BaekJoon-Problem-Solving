from sys import stdin

n = int(stdin.readline())

for i in range(n):
    sentence = list(stdin.readline())

    sentence[0] = sentence[0].upper()

    for i in sentence:
        print(i, end='')

    sentence.clear()