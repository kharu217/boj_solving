S = input()
stack = []
result = ""

is_re = False
for i in S :
    if i == "<" :
        if stack :
            while stack :
                result += stack.pop()
            stack = []
        stack.append(i)
        is_re = True
    elif i == ">" :
        while stack :
            result += stack.pop(0)
        result += ">"
        stack = []
        is_re = False
    elif i == " " :
        if is_re :
            stack.append(i)
        else :
            while stack :
                result += stack.pop()
            result += " "
            stack = []
    else :
        stack.append(i)
while stack :
    result += stack.pop()
        
    
print(result)
