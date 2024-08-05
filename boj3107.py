ip = input()
ip = ip.split(':')
if ip[0] == '':
    ip = ip[1:]
if ip[-1] == '':
    ip = ip[:-1]

res = ''
for i in ip:
    if i=='':
        res += '0000:'*(8-len(ip)+1)
    else:
        res += i.zfill(4)+':'

print(res[:-1])
