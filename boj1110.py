N = int(input())
li = sorted(list(map(int, input().split())))
M = int(input())
box = sorted(list(map(int, input().split())))

if li[-1] < box[-1] :
    print(-1)
    exit()
    

