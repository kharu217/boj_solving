K, N = map(int, input().split())
l = [int(input()) for _ in range(K)]

start, end = 1, max(l)

while start <= end :
    mid = (start + end)//2
    num = 0

    for i in l :
        num += i//mid
    
    if num >= N :
        start = mid + 1
    else :
        end = mid - 1
        
print(end)

