while True :
    N = input()
    temp_l = ''
    
    if N == '.' :
        break
    for i in N :
        if i in '()[]' :
            temp_l += i
        else :
            continue
    
    for _ in range(len(temp_l)//2+1) :
        temp_l = temp_l.replace('()', '')
        temp_l = temp_l.replace('[]', '')
    
    if len(temp_l) :
        print('no')
    else :
        print('yes')
    