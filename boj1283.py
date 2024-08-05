N = int(input())

word_l = [input().split(' ') for _ in range(N)]
short_ct = []

for i in range(len(word_l)) :
    temp_l = list(word_l[i])
    for t in temp_l :
        if t == ' ' :
            continue
        if t.upper() not in short_ct or t not in short_ct:
            short_ct.append(t)
            break
    temp_l.clear()
    
for d in word_l :
    print(d)
