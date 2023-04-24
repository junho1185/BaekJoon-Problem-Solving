A, B = map(int, input().split())
C, D = map(int, input().split())

result = A/C + B/D

result_max = result

rotating_cnt = 0

result = C/D + A/B

if result > result_max:
    rotating_cnt = 1
    result_max = result

result = D/B + C/A

if result > result_max:
    rotating_cnt = 2
    result_max = result

result = B/A + D/C

if result > result_max:
    rotating_cnt = 3
    result_max = result

print(rotating_cnt)