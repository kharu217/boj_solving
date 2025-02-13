import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
l = [-1]*N
stack = [0] # 0번 인덱스

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        l[stack.pop()] = A[i]
    stack.append(i)
print(*l)