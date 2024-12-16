from sys import stdin

# 커서를 중심으로 양쪽에 있는 스택 생성
# 커서를 직접 움직이기보단 값들을 움직여서 커서가 움딕이는 것 같은 효과
left = list(input())
right = []

for _ in range(int(input())) :
    cmd = list(stdin.readline().split())
    # 왼쪽이 비어있으면 커서가 맨 앞에 있다는 의미
    if cmd[0] == 'L' and left :
        right.append(left.pop())
    # 오른쪽이 비어있으면 커서가 맨 뒤에 있다는 의미
    elif cmd[0] == 'D' and right :
        left.append(right.pop())
    elif cmd[0] == 'B' and left :
        left.pop()
    elif cmd[0] == 'P' :
        left.append(cmd[1])

# right를 뒤집어 주는 것은 왼쪽에서 꺼낸 요소들이 오른 쪽에 거꾸로 들어갔기 떄문
answer = left+right[::-1]
print(''.join(answer))
