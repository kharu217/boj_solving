from itertools import combinations

N, M = map(int, input().split())

num_list = []
sum_list = []

num_list = list(map(int, input().split()))

for i in list(combinations(num_list, 3)) :
    sum_list.append(sum(i))

sum_list = list(set(sum_list))

sum_list.sort()

for a in sum_list :
    if a > M :
        del sum_list[sum_list.index(a):]
        break
        
print(sum_list[-1])

