#실제로 문자열을 뒤집는게 아닌 그때그때 최적의 문자열을 한글자씩씩 맞춰가는 식
s = input()
l = s[0]
for i in range(1, len(s)):
    if l[i-1] < s[i] :
        l = s[i]+l
    else :
        l = l+s[i]
print(l[::-1])