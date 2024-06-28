N = int(input())

input_l = []

for i in range(N) :
    input_l.append(input())

for t in input_l :
    print(f'{input_l.index(t) + 1}. {t}')
