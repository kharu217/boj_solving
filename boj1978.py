M = int(input())
N = list(map(int, input().split()))

amount = 0

def is_prime(x) :
    for a in range(2, x) :
        if x % a == 0 :
            return False
    return True

for i in range(M) :
    if N[i] == 1 or N[i] == 0:
        continue
    
    if is_prime(N[i]) == True or N[i] == 2 :
        amount += 1
    
print(amount)
