def same_al(A, B) :
    cnt = 0
    for i in len(A) :
        for t in len(B) :
            if A[i] == B[t] :
                cnt += 1
                break
            else :
                break
    return cnt


A, B = input().split()

smae_
