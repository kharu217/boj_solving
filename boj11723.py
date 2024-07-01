import sys

S = set()
N = int(sys.stdin.readline().rstrip())

for i in range(N) :
    cmd = sys.stdin.readline().rstrip()
    if 'add' in cmd :
        if cmd[-1] not in S :
            S.add(cmd[-1])
        else :
            continue

    elif 'remove' in cmd :
        try :
            S.remove(cmd[-1])
        except :
            continue

    elif 'check' in cmd :
        print(int(cmd[-1] in S))

    elif 'toggle' in cmd :
        if cmd[-1] in S :
            S.remove(cmd[-1])
        else :
            S.add(cmd[-1])

    elif cmd == 'all' :
        S = set(range(1, 21))

    elif cmd == 'empty' :
        S.clear()