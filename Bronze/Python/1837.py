n, k = map(int, input().split())

good_flag = True
for i in range(2, k):
    if n % i == 0:
        print("BAD %d" % i)
        good_flag = False
        break

if good_flag:
    print("GOOD")