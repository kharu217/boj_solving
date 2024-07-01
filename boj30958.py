N = int(input())
S_str = input().lower().replace(' ','')

S = dict()

for i in range(len(S_str)) :
    if S_str[i] in S.keys() :
        S[S_str[i]] += 1
    else :
        S[S_str[i]] = 1
sorted(S.items(), key= lambda item:item[1])

print(max(S.values()))
