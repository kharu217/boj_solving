N = int(input())
text_lists = []
result_list = []

T = []

for i in range(N) :
    T.append(input())

T = list(set(T))
T.sort(key=len)

for a in range(50) :
    temp_lists = []
    for t in T :
        if len(t) == a + 1 :
            temp_lists.append(t)
    temp_lists.sort()
    result_list.extend(temp_lists)

for r_t in result_list :
    print(r_t)
