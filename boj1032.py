n = int(input())
l = list(input())

for s in range(n-1) :
    word = input()
    for i in range(len(word)) :
        if word[i] != l[i] :
            l[i] = '?'
        else :
            continue

for i in l :
    print(i, end='')

