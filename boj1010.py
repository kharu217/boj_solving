from math import factorial

N = int(input())

for i in range(N) :
    A, B = map(int, input().split())
    result = factorial(B)/(factorial(B-A)*factorial(A))

    print(int(result))

