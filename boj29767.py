N, K = map(int, input().split())

class_l = list(map(int, input().split()))

while True :
    S = 0

    for i in range(N) :
        S += class_l[i] * K
        if i == 0 or i == 2 or i == 4 :
            K -= 1

    print(S)
