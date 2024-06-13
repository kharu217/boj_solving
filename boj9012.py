N = int(input())

for i in range(N) :
    input_P = list(input())
    for i in range(len(input_P)) :
        if i == "(" :
            del input_P[i]
            try :
                input_P.remove(')')
            except :
                break
    if len(input_P) == 0 :
        print('YES')
    else :
        print('NO')