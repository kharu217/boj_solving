l = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(l)):
    if l[i] == "(":
        stack.append(l[i])
        tmp *= 2
    elif l[i] == "[":
        stack.append(l[i])
        tmp *= 3
    elif l[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if l[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if l[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)