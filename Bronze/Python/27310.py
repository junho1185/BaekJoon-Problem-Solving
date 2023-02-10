emoji = list(input().strip())
difficulty = 0
difficulty += len(emoji)
difficulty += emoji.count(':')
difficulty += emoji.count('_')*5
print(difficulty)