N = int(input())

for i in range(N) :
    V_l = []
    V = input()

    for a in V :
        if a == '(' :
            V_l.append(a)
        elif a == ')' :
            if V_l :
                V_l.pop()
            else :
                print('NO')
                break
    else :
        if not V_l :
            print('YES')
        else :
            print('NO')