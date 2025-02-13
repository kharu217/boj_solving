d = {chr(i):0 for i in range(97, 123)}

S = input()
for i in S :
    d[i] += 1
print(*d.values())
