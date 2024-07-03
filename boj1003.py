N = int(input())

for _ in range(N) :
    T = int(input())
    a, b = 1, 0
    for i in range(T) :
        a, b = b , a + b
    print(a, b)