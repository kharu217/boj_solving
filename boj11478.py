N = list(input())
set_N = set()

for i in range((len(N))) :
    set_N.add(''.join(N[:i]))
for d in range(len(N)*-1,-1) :
    set_N.add(''.join(N[:i]))
print(set_N)
