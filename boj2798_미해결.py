N, M = map(int, input().split())
card = list(map(int, input().split()))
orig_card = card

result = []

for i in range(N) :
    card.pop(i)
    print(card, 'i')
    for a in range(len(card)) :
        card.pop(a)
        print(card, 'a')
        for h in range(len(card)) :
            result.append(orig_card[i] + orig_card[a] + orig_card[h])
            print(result, "r")
            
for j in result :
    if j > M :
        result.remove(j)
        
result.sort()
print(int(result[-1]))
