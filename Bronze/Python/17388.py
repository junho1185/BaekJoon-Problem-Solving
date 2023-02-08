from sys import stdin
Soongsil, Korea, Hanyang = map(int, stdin.readline().split())

if Soongsil + Korea + Hanyang >= 100:
    print("OK")
elif Soongsil < Korea and Soongsil < Hanyang:
    print("Soongsil")
elif Korea < Soongsil and Korea < Hanyang:
    print("Korea")
else:
    print("Hanyang")