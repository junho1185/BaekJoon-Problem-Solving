from sys import stdin

def is_vowel(i):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        return 1
    elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        return 1
    else:
        return 0

str = stdin.readline().strip()
cnt = 0
while str != "#":
    cnt = 0
    for i in str:
        if is_vowel(i):
            cnt += 1
    print(cnt)
    str = stdin.readline().strip()