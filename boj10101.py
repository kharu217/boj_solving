l = []
same_ang = 0


for i in range(3) :
    l.append(int(input()))

for i in l :
    if l.count(i) > 1 :
        same_ang = l.count(i)
        break

if sum(l) != 180 :
    print('Error')
elif same_ang == 3 :
    print('Equilateral')
elif same_ang == 2 :
    print('Isosceles')
else :
    print('Scalene')
