s = input()
for i in range(1, len(s) + 1) :
    print(s[i-1], end="")
    if i % 10 == 0 :
        print("\n", end="")
    