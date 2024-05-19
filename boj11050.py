from math import factorial

def ihang(N, K) :
    return factorial(N) // (factorial((N - K)) * factorial(K))

N, M = map(int, input().split())
print(ihang(N, M))