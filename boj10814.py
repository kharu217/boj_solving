A=int(input())
user = []
for _ in range(A):
    age, name = input().split()
    user.append([int(age),name])

user.sort(key= lambda x : x[0])

for i in user:
    print(i[0],i[1])