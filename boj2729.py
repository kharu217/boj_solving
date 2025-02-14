n = int(input())

for i in range(n) :
    l = []
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    t = str(bin(a + b))
    print(t[2:])
    
        
