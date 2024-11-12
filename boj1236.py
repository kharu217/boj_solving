W, H = map(int, input().split())
l = []
cnt = 0

for _ in range(W) :
    l.extend(input().split())

#행 탐색
for w in range(W) :
    
    if 'X' not in l[W] :
        cnt += 1
