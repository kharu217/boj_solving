while True :
    input_l = list(map(int, input().split()))
    input_l.sort()
    if input_l == [0,0,0] :
        break
    elif input_l[-1] >= input_l[0] + input_l[1] :
        print('Invalid')
    elif len(set(input_l)) == 1 :
        print('Equilateral')
    elif len(set(input_l)) == 2 :
        print('Isosceles')
    else :
        print('Scalene')