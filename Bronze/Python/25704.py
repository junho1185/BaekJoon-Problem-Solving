stamp = int(input())
price = int(input())
min_pay = price
if stamp >= 20:
    min_pay = price*0.75
if stamp >= 15:
    if price - 2000 < min_pay:
        min_pay = price - 2000
if stamp >= 10:
    if price*0.9 < min_pay:
        min_pay = price*0.9
if stamp >= 5:
    if price - 500 < min_pay:
        min_pay = price - 500

if min_pay < 0:
    print(0)
else:
    print(int(min_pay))