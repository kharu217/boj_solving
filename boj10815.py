import sys

N = int(sys.stdin.readline())
N_l = sorted(list(map(int, sys.stdin.readline().split())))
M = list(map(int, sys.stdin.readline().split()))
M_l = sorted(list(map(int, sys.stdin.readline().split())))

s = dict()

for i in M_l :
    