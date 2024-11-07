N = int(input())
x_l = []
y_l = []

for i in range(N) :
    x, y = map(int, input().split())
    x_l.append(x)
    y_l.append(y)
print((max(x_l) - min(x_l)) * (max(y_l) - min(y_l)))
