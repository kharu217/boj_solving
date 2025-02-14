a, b, c = map(int, input().split())

result = 1
#a^8 -> a^4 * a^4 -> a^2 * a^2 * a^2 * a^2
#a^7 -> a^3 * a^3 * a
while b > 0:
    # b이 홀수인 경우, 결과에 a를 곱하고 b을 하나 감소
    if b % 2 == 1:
        result *= a
        b -= 1
    # a를 제곱하고 b을 반으로 줄임
    a *= a
    b //= 2
    
print(result % c)
