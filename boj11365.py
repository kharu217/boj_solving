while True :
    cmd = list(input())
    if cmd == ['E', 'N', 'D'] :
        break
    cmd.reverse()
    print(''.join(cmd))