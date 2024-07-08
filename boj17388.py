S, K, H = map(int, input().split())

l = [S, K, H]

dict_l = {S : 'Soongsil', 
          K : 'Korea', 
          H : 'Hanyang'}

if sum(l) >= 100 :
    print('OK')
else :
    print(dict_l[min(l)])
