from sys import stdin, stdout
str = stdin.readline().strip()
while str != "END":
    length = len(str)
    for i in range(length):
        stdout.write(str[length - i - 1])
    stdout.write('\n')
    str = stdin.readline().strip()