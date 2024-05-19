T = int(input())

N = [[0,0] for i in range(T)]

for i in N :
    i[0], i[1] = map(int, input().split())
    
n = 1
    
for a in N :
    print(f'Case #{n}:',f'{a[0]} + {a[1]} =', a[1] + a[0])
    n += 1
