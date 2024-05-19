N = int(input())

if N < 5 and N < 3 :
    print(-1)

five_count = 0
three_count = 0

while N >= 3 :
    N -= 3
    three_count += 1

while N >= 5 :
        N -= 5
        five_count += 1
    
print(five_count, ",", three_count)  
