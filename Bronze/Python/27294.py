t, s = map(int, input().split())
if s == 1:
    rice = 280
else:
    if 11 < t and t < 17:
        rice = 320
    else:
        rice = 280
print(rice)