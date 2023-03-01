word = input().strip()
vowel_cnt = 0

for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowel_cnt += 1
print(vowel_cnt)