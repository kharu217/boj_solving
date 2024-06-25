from sys import stdin

N = int(stdin.readline())
My_card = list(map(int, stdin.readline().split()))

M = int(input())
oppos_card = list(map(int, stdin.readline().split()))

re_dict = dict()

for i in oppos_card :
    if i in re_dict :
        re_dict += 1
    else :
        re_dict[i] = 0

for t in My_card :
    try :
        re_dict[i] += 1
    except :
        continue

for s in re_dict.values() :
    print(s, end=' ')