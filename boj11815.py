n = int(input())
l = list(map(int, input().split()))

#약수는 한쌍씩 존재하므로 ex)6 = 1 * 6, 2 * 3 등
#제곱수는 자기자신과 그의 제곱근이 약수이므로 제곱근을 판별하면 됨됨
for i in l :
    if i == (int(i ** 0.5) ** 2) :
        print(1, end=" ")
    else :
        print(0, end=" ")
