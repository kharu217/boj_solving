S = input()
stack = []
result = ""

#알파벳은 일단 답에 모두 추가하고 기호만 남기는 방식
for i in S :
    #괄호가 열리면 일단 append
    if i == "(" :
        stack.append(i)
    #그후 괄호가 닫히면 괄호안의 기호 답에 추가(괄호가 닫힐때까지)
    elif i == ")" :
        while stack and stack[-1] != "(" :
            result += stack.pop()
        stack.pop()
    elif i == "*" or i == "/" :
        while stack and (stack[-1] == "*" or stack[-1] == "/") :
            result += stack.pop()
        stack.append(i)
    elif i == "+" or i == "-" :
        while stack and stack[-1] != "(" :
            result += stack.pop()
        stack.append(i)
    else :
        result += i
while stack :
    result += stack.pop()

print(result)