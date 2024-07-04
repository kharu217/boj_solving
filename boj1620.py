N ,M = map(int , input().split())
poke = dict()
num_poke = dict()

for i in range(N) :
    temp = input()
    poke[temp] = i + 1
    poke[i + 1] = temp
for t in range(M) :
    ans = input()
    if ans.isdecimal() :
        print(poke[int(ans)])
    else :
        print(poke[ans])