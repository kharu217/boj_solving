A, B = map(int, input().split())
if A == B :
    print(0)
    exit()

if A > B :
    A = A ^ B
    B = A ^ B
    A = A ^ B
print(B - A - 1)
for i in range(A+1, B) :
    print(i, end=" ")