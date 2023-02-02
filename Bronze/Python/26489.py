cnt = 0
while True:
    try:
        str = input()
        if str == "gum gum for jay jay":
            cnt += 1
    except EOFError:
        break
print(cnt)