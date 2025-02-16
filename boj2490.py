yut = ["E", "A", "B", 'C', "D"]
for i in range(3) :
    l = list(map(int, input().split()))
    print(yut[-sum(l)-1])