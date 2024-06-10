import sys

N = int(sys.stdin.readline().rstrip())
nums = []

for i in range(N) : 
    a = int(sys.stdin.readline().rstrip())
    nums.append(a)
    
nums.sort()
for a in nums :
    print(a)