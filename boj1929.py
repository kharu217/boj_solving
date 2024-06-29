import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아니다.
    return True

N, M = map(int, input().split())

while N < M :
        if N == 1 :
            N += 1
            continue
        if is_prime_number(N) :
            print(N)
        N += 1
        
if is_prime_number(M) :
    print(M)