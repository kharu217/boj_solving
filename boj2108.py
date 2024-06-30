import sys
input = sys.stdin.readline

N = int(input())

aver = 0
mid_l = 0
many = 0
range_l = 0

l = []
temp = dict()

for i in range(N) :
    tmp_l = int(input())
    l.append(tmp_l)
    if tmp_l in temp.keys() :
        temp[tmp_l] += 1
    else :
        temp[tmp_l] = 1

l.sort()

aver = round(sum(l)/N + 1e-9)
mid_l = l[N//2]

freq = max(temp.values())
numbers = []
for key, value in temp.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    many = numbers[0]
else:
    many = sorted(numbers)[1]

range_l = l[-1] - l[0]

print(aver)
print(mid_l)
print(many)
print(range_l)
