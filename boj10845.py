N = int(input())

queue = []

for i in range(N) :
    cmd = input()

    if 'push' in cmd :
        queue.append(int(cmd[-1]))
    elif cmd == 'pop' :
        try :
            print(queue.pop(0))
        except :
            print(-1)
    elif cmd == 'size' :
        print(len(queue))
    elif cmd == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif cmd == 'front' :
        try :
            print(queue[0])
        except :
            print(-1)
    elif cmd == 'back' :
        try :
            print(queue[-1])
        except :
            print(-1)