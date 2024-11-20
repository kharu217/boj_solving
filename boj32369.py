N, A, B = map(int, input().split())

good = 1
bad = 1

for i in range(N) :
    if bad > good :
        temp = bad
        bad = good
        good = temp
    good += A
    bad += B
if bad == good :
    bad -= 1
print(good, bad)