import math

def is_prime(n) :
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

M = int(input())
N = int(input())

if M == N == 1 :
    print(-1)
    exit()

l = []
for i in range(M, N + 1) :
    if is_prime (i) :
        l.append(i)
if M == 1 :
    l.pop(0)
if len(l) == 0 :
    print(-1)
    exit()  
print(sum(l))
print(min(l))

