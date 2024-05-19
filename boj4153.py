while True :
    N = list(map(int, input().split()))
    
    N_max = max(N)
    N.remove(N_max)
    
    N_min = min(N)
    N.remove(N_min)
    
    N_middle = N[0]
    
    if N_max == 0 and N_min == 0 and N_middle == 0 :
        break
    
    if pow(N_max, 2) == ((N_min ** 2) + (N_middle ** 2)) :
        print("right")
    else :
        print("wrong")
    