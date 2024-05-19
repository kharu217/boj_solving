N = [0,0,0]
N[0], N[1], N[2] = map(int, input().split())

N_length = len(set(N))

if N_length == 1 :
    print(10000 + (N[0] * 1000))
elif N_length == 2 :
    print(1000 + (max(set(N), key=N.count) * 100))
elif N_length == 3:
    print(100 * max(N))