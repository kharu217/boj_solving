N = int(input())
ch_N = N

pre_N = ch_N
cnt = 0

while True :
    if ch_N < 10 :
        ch_N = int(str(pre_N)[-1] + str(ch_N))
    else :
        ch_N = int(str(pre_N)[-1] + str(int(str(ch_N)[0]) + int(str(ch_N)[1]))[-1])
    cnt += 1
    pre_N = ch_N
    if ch_N == N :
        break

print(cnt)
