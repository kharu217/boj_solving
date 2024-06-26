N, M = map(int, input().split())
basket = [0 for i in range(N)]

for i in range(M) :
    get_v = list(map(int, input().split()))
    if get_v[0] == get_v[1] :
        basket[get_v[0]-1:get_v[1]] = [get_v[2] for _ in range(get_v[0], get_v[1]+1)]
    else :
        basket[get_v[0]-1:get_v[1]] = [get_v[2] for _ in range(get_v[0], get_v[1]+1)]

for l in basket :
    print(l, end=' ')