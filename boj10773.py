N = int(input())
l = []

for i in range(N) :
    temp = int(input())
    
    if temp == 0 :
        l.pop(-1)
        continue
    
    l.append(temp)
    
    
print(sum(l))
