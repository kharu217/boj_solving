import sys
n=int(sys.stdin.readline())

if n == 1 :
    print('*')
    exit()

ans=[" "*(n-i)+"*"*(2*i-1) for i in range(1,n+1)]
ans=ans+ans[n-2::-1]
for s in ans:
    print(s)