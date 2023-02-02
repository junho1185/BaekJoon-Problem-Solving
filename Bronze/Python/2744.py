str = input()
result = []
gap = ord('a') - ord('A')
for i in range(len(str)):
    ch = ord(str[i])
    if 'a' <= str[i] < 'z':
        ch -= gap
    else:
        ch += gap
    result.append(chr(ch))
for i in result:
    print(i, end='')