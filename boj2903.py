N = int(input())
W = 2

for i in range(N) :
    W += 2 ** i
print(W ** 2)