n = int(input())
l = list(map(int, input().split()))

y = 10
m =  15
for i in l :
    temp = i - 29
    i -= 59
    while temp > 0 :
        temp -= 29
        y += 10
    while i > 0 :
        i -= 59
        m += 15
if y < m :
    print("Y", y)
elif m < y :
    print("M", m)
else :
    print("Y M", y)