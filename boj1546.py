M = int(input())

N = list(map(int, input().split()))
new_N = [0 for i in range(M)]
result = 0

max_N = max(N)

for a in range(M) :
    new_N[a] = (N[a] / max_N) * 100
    
for b in range(len(new_N)) :
    result += new_N[b]

print(result/len(new_N))
