
#실패
# import sys

# input = lambda : sys.stdin.readline().rstrip()

# N = int(input())
# M = int(input())
# S = input()

# test_N = 'IO' * N + 'I'
# cnt = 0

# i = 0

# while i <= (M - (N * 2 + 1)) :
#     if S[i] == 'O' :
#         i += 1
#         continue
#     if hash(S[i:i+(N*2+1)]) == hash(test_N) :
#         if S[i:i+N*2+1] == test_N :
#             cnt += 1
#             i += 2
#     else :
#         i += 1
#         continue
# print(cnt)

#성공
N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
