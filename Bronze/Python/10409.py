from sys import stdin

n, T = map(int, stdin.readline().split())

times = list(map(int, stdin.readline().split()))

CPU_Time = 0

process_number = 0

for time in times:
    CPU_Time += time
    if CPU_Time <= T:
        process_number += 1

print(process_number)