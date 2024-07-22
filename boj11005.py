N, B = map(int, input().split())

l = []

while N :
    if N % B >= 10 :
        l.append(chr(N % B + 55))
    else :
        l.append(str(N % B))
    N //= B
l.reverse()

print(''.join(l))
