N = int(input())

for _ in range(N) :
    temp_l = dict()
    for i in range(int(input())) :
        cloth, type_c = input().split()
        if type_c not in temp_l.keys() :
            temp_l[type_c] = [cloth]
        else :
            temp_l[type_c].append(cloth)
    
    for t in range(len(temp_l.keys())) :
        
