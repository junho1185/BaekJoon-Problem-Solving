from sys import stdin

n = int(stdin.readline())

phone_record = list(map(int, stdin.readline().split()))

y_bill = 0
m_bill = 0

for record in phone_record:
    y_bill += (record//30 + 1)*10
    m_bill += (record//60 + 1)*15

if y_bill < m_bill:
    print("Y", y_bill)
elif y_bill > m_bill:
    print("M", m_bill)
else:
    print("Y M", y_bill)