import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
l = list(map(int, input().split()))

f_o_b = True

while True :
    if len(set(l)) <= 2 :
        break
    del l[-1]
    del l[0]
        
    f_o_b = not f_o_b
print(len(l))