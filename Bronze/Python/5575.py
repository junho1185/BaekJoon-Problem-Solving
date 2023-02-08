from sys import stdin
def get_ints():
    return list(map(int, stdin.readline().split()))
workers = []
workers.append(get_ints())
workers.append(get_ints())
workers.append(get_ints())

for i in range(3):
    h = workers[i][3] - workers[i][0]
    m = workers[i][4] - workers[i][1]
    s = workers[i][5] - workers[i][2]

    if s < 0:
        m -= 1
        s += 60
    if m < 0:
        h -= 1
        m += 60
    print(h, m, s)