bits = [int(bit) for bit in input().split()]
cnt = bits.count(9)

if cnt > 0:
    print("F")
else:
    print("S")