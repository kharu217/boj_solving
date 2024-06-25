from sys import stdin

N = int(input())
N_list = set((map(int, stdin.readline().split())))

M = int(input())
M_list = list(map(int, stdin.readline().split()))

for i in M_list :
    if i in N_list :
        print(1)
    else :
        print(0)
