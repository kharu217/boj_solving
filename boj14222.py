import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

temp_l = []

cur_t = 1

while True :
    if min(l) > cur_t :
        print(0)
        break
    if cur_t in l :
        temp_l.append(l.pop(l.index(cur_t)))
        cur_t += 1
    else :
        l[l.index(min(l))] += K
    
    if not l :
        print(1)
        break
