n = int(input())
l = list(map(int, input().split()))
l_2 = l.copy()

stack = []
result = []

f = 1
try :
    while True :
        if result == sorted :
            break
        if not l or l[0] != f :
            if stack and stack[-1] == f:
                result.append(stack.pop())
                f += 1
            elif not l :
                stack.append(l.pop(0))
        else :
            result.append(l.pop(0))
            f += 1
except EOFError :
    print("Sad")
else :
    print("Nice")