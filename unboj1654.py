import bisect

N, M = map(int, input().split())

lan_l = []

for i in range(N) :
    lan_l.append(int(input()))

lan_l.sort()

result = 0

low = 1
high = max(lan_l)
mid = max(lan_l) // 2

while True :
    sum_l = 0

    for i in lan_l :
        sum_l += int(i/mid)

    if sum_l <= M :
        low = mid + 1
    else :
        high = mid - 1
    
    if high <= low :
        result = low
        break

print(low)
