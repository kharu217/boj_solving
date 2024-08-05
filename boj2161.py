N = int(input())
l = [i for i in range(1, N + 1)]

while l :
    try :
        print(l.pop(0), end=' ')
        l.append(l.pop(0))
    except :
        break
