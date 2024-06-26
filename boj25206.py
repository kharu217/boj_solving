rate = {'A+' : 4.5,
        'A0' : 4.0,
        'B+' : 3.5,
        'B0' : 3.0,
        'C+' :2.5,
        'C0' : 2.0,
        'D+' :1.5,
        'D0' : 1.0,
        'F' : 0.0}

score_l = []
rate_score = []

for i in range(20) :
    name, score, rate_l = tuple(input().split())
    if rate_l == 'P' :
        continue
    else :
        rate_score.append(rate[rate_l])
        score_l.append(float(score))

result = 0
for n in range(len(rate_score)) :
    result += score_l[n] * rate_score[n]

print(result/sum(score_l))