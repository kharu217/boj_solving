n, k = map(int, input().split())

coin_v = sorted([int(input()) for _ in range(n)])

l = [100001] * (k + 1)
l[0] = 0

for coin in coin_v :
    for i in range(coin, k + 1) :
        l[i] = min(l[i], l[i - coin] + 1)

if l[-1] == 100001 :
    print(-1)
else :
    print(l[-1])
#i 인덱스로 뒀을때 그 i원을 만들수 있는 최소 동전의 개수를 i번째에다가 넣는거임
#