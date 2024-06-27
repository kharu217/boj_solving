L = int(input()) #길이
A = int(input()) #국어
B = int(input()) #수학
C = int(input()) #국어
D = int(input()) #수학
Kor, Math = 0, 0 
count = 0
while True:
    if A >= C or B >= D:
        Kor += C
        Math += D
        count += 1
    if A <= Kor and B <= Math:
        print(L-count)
        break