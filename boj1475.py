S = list(input())

cnt = 0

while S :
    l = [str(i) for i in range(1, 10)]
    cnt += 1
    i = 0
    while i < len(S) :
        if S[i] in l :
            S.remove(S[i])
            l.remove(S[i])
        elif (S[i] == '9' and '6' in l) :
            S.remove(S[i])
            l.remove('6')
        elif (S[i] == '6' and '9' in l) :
            S.remove(S[i])
            l.remove('9')
        i += 1

print(cnt)
