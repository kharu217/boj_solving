l = list(input().split())
fA, fB = input().split()

A = []
B = []
for a in fA :
    A.append(str(l.index(a)))
for b in fB :
    B.append(str(l.index(b)))
A = int(''.join(A))
B = int(''.join(B))
total = str(A + B)

result = ''
for t in total :
    result += l[int(t)]
print(result)
