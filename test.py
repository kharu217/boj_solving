N = int(input())
cnt_ = [0,0]

def fib(n) :
    if n == 0 :
        cnt_[0] += 1
    elif n == 1 :
        cnt_[1] += 1
    else :
        fib(n - 1)
        fib(n - 2)

for i in range(N) :
    temp = int(input())
    fib(temp)
    print(cnt_[0], cnt_[1])
    cnt_ = [0,0]