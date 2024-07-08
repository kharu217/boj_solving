M = list(map(int, input().split()))
N = int(input())

if sum(M) < N * 2 :
    print(sum(M))
else :
    print(sum(M) - N * 2)
