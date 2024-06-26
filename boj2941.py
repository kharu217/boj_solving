N = input()
cro_A = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

n_count = len(N)

for i in cro_A :
    n_count -= N.count(i)

print(n_count)
