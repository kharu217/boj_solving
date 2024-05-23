N = int(input())
L = input()

sum = 0

for i in range(N) :
    sum += (ord(L[i]) - 96) * 31**i

print(sum % 1234567891)