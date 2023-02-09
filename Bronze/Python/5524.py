n = int(input())
for i in range(n):
    str = input().strip()
    for letter in str:
        if ord('A') <= ord(letter) <= ord('Z'):
            print(chr(ord(letter) + (ord('a') - ord('A'))), end='')
        else:
            print(letter, end='')
    print()