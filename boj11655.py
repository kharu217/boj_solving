S = input()
l = []

for i in S :
    uni = ord(i)
    if 65 <= uni <= 90 :
        uni += 13
        if uni > 90 :
            uni -= 90
            uni += 64
    elif 97 <= uni <= 122 :
        uni += 13
        if uni > 122 :
            uni -= 122
            uni += 96
    else :
        pass
    l.append(uni)

print("".join(map(chr, l)))
