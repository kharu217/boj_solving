import decimal
import sys

input = sys.stdin.readline

N = int(input())

l = []
for i in range(N) :
    l.append(decimal.Decimal(input()))
l.sort()
print(*l[:7], sep='\n')
    