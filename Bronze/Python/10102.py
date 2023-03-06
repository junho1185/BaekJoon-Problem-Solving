n = int(input())
judge = input()
a_cnt = 0
b_cnt = 0

for i in judge:
    if i == 'A':
        a_cnt += 1
    elif i == 'B':
        b_cnt += 1

if a_cnt > b_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")
else:
    print("Tie")