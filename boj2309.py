from itertools import combinations

l = []
for _ in range(9) :
    l.append(int(input()))

comb = list(combinations(l, 7))
for i in comb :
    if sum(i) == 100 :
        print(*sorted(i), sep="\n")
        break