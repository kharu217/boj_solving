import sys

WB_lambda = lambda x : 'B' if x == 'W' else 'W'

H, W = map(int, sys.stdin.readline().rstrip().split())

chess_board = []

cnt = 0
pre_t_f = ''
pre_t = ''

for i in range(H) :
    temp_t = list(sys.stdin.readline().rstrip())
    for n in range(W) :
        #맨 앞
        if i == 0 and n == 0 :
            pre_t_f = temp_t[n]
        
        elif n == 0 and temp_t[n] == pre_t_f:
            temp_t[n] = WB_lambda(temp_t[n])
            pre_t_f = temp_t[n]
            pre_t = temp_t[n]
            cnt += 1

        elif n == 0 :
            pre_t_f = temp_t[n]
            pre_t = temp_t[n]
        
        elif temp_t[n] == pre_t :
            temp_t[n] = WB_lambda(temp_t[n])
            pre_t = temp_t[n]
            cnt += 1

            
print(cnt)