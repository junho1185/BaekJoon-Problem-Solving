from sys import stdin

c, k, p = map(int, stdin.readline().split())

sum_of_wines = 0

for year in range(1, c + 1):
    sum_of_wines += k*year + p*year*year

print(sum_of_wines)