N = input()

if N[0] == '"' and N[-1] == '"' :
    N = N.strip('"')
    if bool(N.replace(' ', '')) == False:
        print('CE')
    else :
        print(N)
else :
    print('CE')
