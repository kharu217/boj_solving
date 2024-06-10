N = list(map(int, input().split()))

sum = 0

for i in N :
    sum += i ** 2

print(sum % 10)
