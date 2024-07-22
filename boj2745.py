N, B = input().split()
B = int(B)
N = list(N)
N.reverse()

for s in range(len(N)) :
    if N[s].isalpha() :
        N[s] = ord(N[s]) - 55
    elif N[s].isdigit() :
        N[s] = int(N[s])
        
cnt = 0

for i in range(len(N)) :
    cnt += N[i] * (B ** i)
print(cnt)