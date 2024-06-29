import sys

input = sys.stdin.readline

diff_l = []

N = int(input())

if N == 0 :
    print(0)
    exit()

for i in range(N) :
    diff_l.append(int(input()))

diff_l.sort()
diff_l_c = diff_l.copy()

diff_c_aver = round((len(diff_l) * 0.3)/2 + 1e-9)

try :
    del diff_l[0:diff_c_aver]
    del diff_l[diff_c_aver * -1:]
    print(round(sum(diff_l)/len(diff_l) + 1e-9))
except :
    print(round(sum(diff_l_c)/len(diff_l_c) + 1e-9))