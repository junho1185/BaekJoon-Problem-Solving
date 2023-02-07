from sys import stdin
def get_ints():
    return list(map(int, stdin.readline().split()))
mingook = get_ints()
manse = get_ints()
S = 0
T = 0
for i in mingook:
    S += i
for i in manse:
    T += i
if S > T:
    print(S)
else:
    print(T)