n = int(input())
l = list(map(int, input().split()))
process_n = int(input())

temp_l = []

for i in range(0, n, n//process_n) :
    temp = l[i:i+n//process_n]
    temp.sort()
    for j in temp:
        print(j, end=' ')
