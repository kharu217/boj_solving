import sys

S = set()
N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    cmd = sys.stdin.readline().rstrip()
    try :
        argu = int(cmd[-2:].rstrip(' '))
    except :
        pass
    if 'add' in cmd :
        if argu not in S :
            S.add(argu)
        else :
            continue

    elif 'remove' in cmd :
        try :
            S.remove(argu)
        except :
            continue

    elif 'check' in cmd :
        print(int(argu in S))

    elif 'toggle' in cmd :
        if argu in S :
            S.remove(argu)
        else :
            S.add(argu)

    elif cmd == 'all' :
        S = set(range(1, 21))

    elif cmd == 'empty' :
        S.clear()