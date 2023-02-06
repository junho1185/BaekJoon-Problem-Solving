import sys
def get_ints():
    return map(int, sys.stdin.readline().strip().split())

r1, s = get_ints()

r2 = 2*s - r1

sys.stdout.write(str(r2))