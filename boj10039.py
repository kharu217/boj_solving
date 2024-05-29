result = 0

for i in range(5) :
    A = int(input())
    if A < 40 : 
        result += 40
    else :
        result += A

print(result//5)
