X = int(input())
N = int(input())

item = [[0,0] for i in range(N)]
total = 0

for i in item :
    i[0], i[1] = map(int, input().split())
    
for a in item :
    total += a[1] * a[0]
    
if total == X :
     print('Yes')
else :
    print('No')
