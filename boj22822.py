l = [(int(input()), i+1) for i in range(8)]
l.sort(reverse=True)

result = 0
result_l = []

for t in range(5) :
    result += l[t][0]
    result_l.append(l[t][1])

result_l.sort()

print(result)

for c in result_l :
    print(c, end=' ')
