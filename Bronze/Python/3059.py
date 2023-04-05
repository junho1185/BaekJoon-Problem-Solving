from sys import stdin

n = int(stdin.readline())

for i in range(n):
    sentence = stdin.readline().strip()
    non_existing_sum = 0

    for character in range(ord('A'), ord('Z') + 1):
        if sentence.count(chr(character)) == 0:
            non_existing_sum += character
    
    print(non_existing_sum)