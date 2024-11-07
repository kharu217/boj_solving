x_l = []
y_l = []
for i in range(3) :
    x, y = map(int, input().split())
    x_l.append(x)
    y_l.append(y)
x_l.sort()
y_l.sort()

less_y = y_l[0]
if y_l.count(less_y) > y_l.count(y_l[-1]) :
    less_y = y_l[-1]

less_x = x_l[0]
if x_l.count(less_x) > x_l.count(x_l[-1]) :
    less_x = x_l[-1]
print(less_x, less_y)
