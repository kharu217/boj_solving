import sys

class stack :
    stack_l = []

    def empty(self) :
        if len(self.stack_l) == 0 :
            return 1
        else :
            return 0

    def push(self, x) :
        self.stack_l.append(x)

    def pop(self) :
        if self.empty(self) == 1:
            return -1
        else :
            return self.stack_l.pop(-1)
        
    def size(self) :
        return len(self.stack_l)
    
    def top(self) :
        if self.empty(self) == 0:
            return self.stack_l[-1]
        else : 
            return -1



n_stack = stack
N = int(input())

for i in range(N) :
    cmd_n = sys.stdin.readline().rstrip().split()
    current_cmd = cmd_n[0]

    if current_cmd == 'push' :
        n_stack.push(n_stack ,cmd_n[1])
    elif current_cmd == 'pop' :
        print(n_stack.pop(n_stack))
    elif current_cmd == 'size' :
        print(n_stack.size(n_stack))
    elif current_cmd == 'empty' :
        print(n_stack.empty(n_stack))
    elif current_cmd == 'top' :
        print(n_stack.top(n_stack))
