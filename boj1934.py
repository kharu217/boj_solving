def GCD(x, y) :
    while (y) :
        x, y = y, x%y

    return x

def LCM(x, y) :
    result = (x*y)//GCD(x, y)
    return result

N = int(input())

for n in range(N) :
    a, b = map(int, input().split())
    print(LCM(a, b))
