S = input()[::-1]
l = []
temp = ""

for i in S :
    temp += i
    l.append(temp[::-1])
l.sort()
print("\n".join(l))
