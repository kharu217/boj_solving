from collections import deque

N, M = map(int, input().split())
get_num = list(map(int, input().split()))

temp_num = get_num.copy()

l = deque([i + 1 for i in range(N)])

cnt = 0
index = 0

while get_num :
    if l[0] == temp_num[index] :
        l.popleft()
        get_num.pop(0)
        index += 1
    elif l.index(temp_num[index]) < len(l)/2 :
        l.append(l.popleft())
        cnt += 1
    else :
        l.appendleft(l.pop())
        cnt += 1
print(cnt)
