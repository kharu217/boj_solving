import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

del_addr = 0
next_addr = K - 1

Y_list = [p_num for p_num in range(1, N + 1)]
del_list = []


while Y_list :
    del_list.append(Y_list.pop(next_addr))
    next_addr += K - 1

    while next_addr >= len(Y_list) :
        next_addr -= len(Y_list)

        if len(Y_list) == 0 :
            break

del_list = map(str, del_list)

print('<' + ', '.join(del_list) + '>')