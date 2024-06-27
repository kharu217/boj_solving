N = []
next_num = 0

for i in range(3) :
    N.append(input())

for t in N :
    try :
        next_num = int(t) + (len(N) - N.index(t))
    except :
        continue
    
if next_num % 3 == 0 and next_num % 5 == 0 :
    print('FizzBuzz')
elif next_num % 3 == 0 :
    print("Fizz")
elif next_num % 5 == 0 :
    print("Buzz")
else :
    print(next_num)
