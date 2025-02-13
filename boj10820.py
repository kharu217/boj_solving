try :
    while True :
        lower, capital, number, blank = 0, 0, 0, 0
        S = input()
        for i in S :
            if i == " " :
                blank += 1
                continue
            elif i.isdigit() :
                number += 1
                continue
            elif i == i.upper() :
                capital += 1
                continue
            elif i == i.lower() :
                lower += 1
        print(lower, capital, number, blank)
except :
    exit()
    