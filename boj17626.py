from math import sqrt

N = int(input())
dp = []

i = 0
t_res = 0

while N :
    if int(sqrt(N)) != sqrt(N):
        N -= 1
        t_res += 1
    else :
        dp.append(sqrt(N))
        if t_res == 1:
            continue
        N = t_res
    

print(len(dp))        
