import math

MAX = 1000000
prime = [True for i in range(MAX+1)]

prime[1] = False

for i in range(2, int(math.sqrt(MAX))+1):
    if prime[i] == True:
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j += 1

n = int(input())
while n != 0 :
    for i in range(2, n - 1) :
        if prime[i] and prime[n - i] :
            print(f"{n} = {i} + {n - i}")
            break
    else :
        print("Goldbach's conjecture is wrong.")
    n = int(input())
