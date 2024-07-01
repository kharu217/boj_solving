N , M = map(int, input().split())
l = set([input() for i in range(N)])
s_l = set([input() for i in range(M)])

result = list(s_l & l)

result.sort()
print(len(result))

for _ in result :
    print(_)
