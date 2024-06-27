ham = []
d = []

for i in range(3) :
    ham.append(int(input()))
for _ in range(2) :
    d.append(int(input()))

print(min(ham) + min(d) - 50)
