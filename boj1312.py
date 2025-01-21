import decimal

A, B, N = map(int, input().split())
decimal.getcontext().prec = 1000002

S = str(decimal.Decimal(A)/decimal.Decimal(B))
try : 
    print(S.split('.')[1][N - 1])
except IndexError :
    print(0)
