N = int(input())
S = list(input())

stack = []

n_list = []
for i in range(N) :
    n_list.append(int(input()))

symbol = ["*", "/", "-", "+"]
#읽다가 기호가 나오면 뒤의 숫자랑 계산하면 되는거아님?
for sym in S :
    if sym not in symbol :
        stack.append(sym)
    elif sym in symbol :
        caled1 = n_list[ord(stack.pop()) - 65] if type(stack[-1]) == str else stack.pop()
        caled2 = n_list[ord(stack.pop()) - 65] if type(stack[-1]) == str else stack.pop()
        if sym == "+" :
            temp_r = caled2 + caled1
        elif sym == "-" :
            temp_r = caled2 - caled1
        elif sym == "*" :
            temp_r = caled2 * caled1
        elif sym == "/" :
            temp_r = caled2 / caled1
        stack.append(temp_r)
print("{:.2f}".format(*stack))