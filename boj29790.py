N, U, L = map(int, input().split())

if N >= 1000 :
    if U >= 8000 :
        if L >= 260 :
            print("Very Good")
        else :
            print("Bad")
    else :
        print("Good")
else :
    print("Good")
