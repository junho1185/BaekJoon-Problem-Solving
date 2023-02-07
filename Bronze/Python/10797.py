import sys

ten_bu = int(sys.stdin.readline())
cars = list(map(int, sys.stdin.readline().split()))

print(cars.count(ten_bu))