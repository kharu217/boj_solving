N_str = list(input())
N = int(input())

cursor = len(N_str)
max_c = len(N_str)

for i in range(N) :
    cmd = input()
    if 'D' in cmd :
        if cursor == max_c :
            continue
        cursor += 1
    elif 'L' in cmd :
        if cursor == 1 :
            continue
        cursor -= 1
    elif 'B' in cmd :
        if cursor == 1 :
            continue
        del N_str[cursor - 1]
        cursor -= 1
    else :
        N_str.insert(cursor - 1, cmd[-1])
    
print(''.join(N_str))