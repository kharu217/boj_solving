S = input()
bomb = input()
stack = []

n_bomb = len(bomb)

for i in range(len(S)) :
    stack.append(S[i])
    if "".join(stack[-n_bomb:]) == bomb :
        for b in range(n_bomb) :
            stack.pop()

if stack :
    print(''.join(stack))
else :
    print("FRULA")
