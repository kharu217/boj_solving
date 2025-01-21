s = list(input())
s.append(' ')
reverse_word = []
temp_word = []
result = []

is_unreverse = False
for char in s :
    if char == '<' :
        is_unreverse = True
        temp_word.append(char)
        if reverse_word :
            result.append(''.join(reverse_word[::-1]))
            reverse_word = []
            continue
    elif char == '>' :
        is_unreverse = False
        temp_word.append(char)
        result.append(''.join(temp_word))
        temp_word = []
        continue
    elif char == ' ' and not is_unreverse:
        result.append(''.join(reverse_word[::-1]))
        reverse_word = []
        continue
    if is_unreverse :
        temp_word.append(char)
    else :
        reverse_word.append(char)   
print(result)