N = list(input())
l = ['U', 'C', 'P', 'C']
tmp_l = []

i = 0
try :
    while True :
        if i == 4 :
            break
        if N[i] == l[i] :
            tmp_l.append(N[i])
        else :
            del N[i]
            i -= 1
        i += 1
    if tmp_l == l :
        print('I love UCPC')
except :
    print('I hate UCPC')
        