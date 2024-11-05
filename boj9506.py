while True :
    num = int(input())

    if num == -1 :
        break

    l = []
    str_l = []
    for i in range(1, num + 1) :
        if i == num :
            break
        if num % i == 0 :
            str_l.append(str(i))
            l .append(i)

    if sum(l) == num :
        print(f'{num} =',' + '.join(str_l))
    else :
        print(f'{num} is NOT perfect.')
