import sys
from collections import deque

N = int(sys.stdin.readline())

for i in range(N) :
    cmd = sys.stdin.readline().strip()
    l_len = int(sys.stdin.readline())
    try :
        temp_l = deque(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    except :
        temp_l = []
    is_reverse = False
    # try :
    #     l_list = deque(map(int, temp_l[1:-1].split(',')))
    # except :
    #     l_list = deque([])
    for t in cmd :
        if t == 'R' :
            is_reverse = not is_reverse
        elif t == 'D' :
            if len(temp_l) == 0 :
                print('error')
                break
            else :
                if is_reverse :
                    temp_l.pop()
                else :
                    temp_l.popleft()
    else :
        if is_reverse :
            temp_l.reverse()
            print(str(list(temp_l)).replace(' ', ''))
        else :
            print(str(list(temp_l)).replace(' ', ''))