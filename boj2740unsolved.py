A = []
B = []
N, M = map(int, input().split())
for i in range(N) :
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for w in range(M) :
    B.append(list(map(int, input().split())))

div_mat = []
for w in range(M) :
    temp = []
    for h in range(M) :
        temp.append(A[h][w]*B[w][h])
        print(w, h)
    div_mat.append(sum(temp))
print(div_mat)