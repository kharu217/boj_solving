N = 1

dict_l = {'0' : 4,
          '1' : 2,}

while True :
    N = input()
    if N == '0' :
        break
    result = 2 + (len(N) - 1)
    for i in N :
        if i in dict_l.keys() :
            result += dict_l[i]
        else :
            result += 3
    print(result)