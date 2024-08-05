l = []
for i in range(2, 9876543211) :
    if str(i)[::-1] == ''.join(sorted(list(str(i)))) :
        l.append(i)

N = int(input())
print(l[N - 1])
