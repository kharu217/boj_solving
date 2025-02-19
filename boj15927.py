s = list(input())
revers_s = list(reversed(s))

if len(set(s)) == 1 :
    print(-1)
elif s == revers_s :
    print(len(s) - 1)
else :
    print(len(s))