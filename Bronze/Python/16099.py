n = int(input())
for i in range(n):
    w1, l1, w2, l2 = map(int, input().split())
    if(w1*l1 > w2*l2):
        print("TelecomParisTech")
    elif(w1*l1 == w2*l2):
        print("Tie")
    else:
        print("Eurecom")