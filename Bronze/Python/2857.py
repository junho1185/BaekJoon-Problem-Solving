from sys import stdin

FBI_cnt = 0

detection = []

for i in range(5):
    name = stdin.readline()
    if name.find('FBI') >= 0:
        FBI_cnt += 1
        detection.append(i+1)

if FBI_cnt == 0:
    print("HE GOT AWAY!")
else:
    for name in detection:
        print(name, end = ' ')
    print()