N = int(input())

Q = 0
D = 0
NI = 0
P = 0

for _ in range(N) :
    temp = int(input())
    while temp >= 25 :
        temp -= 25
        Q += 1
        
    while temp >= 10 :
        temp -= 10
        D += 1
        
    while temp >= 5 :
        temp -= 5
        NI += 1
        
    while temp >= 1 :
        temp -= 1
        P += 1
    print(Q, D, NI, P)
    Q = 0
    D = 0
    NI = 0
    P = 0

