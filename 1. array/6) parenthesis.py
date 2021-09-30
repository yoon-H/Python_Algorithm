import sys

class Stack:
    # make stack
    def __init__ (self):
        self.top = []
    
    # print stack size
    def __len__(self):
        return len(self.top)

    # PUSH
    def push (self, item):
        self.top.append(item)

    # POP
    def pop(self):
        # if Stack is not empty
        return self.top.pop(-1)
    
    # read the value of top in stack
    def peek(self):
        if not self.isEmpty(self):
            return self.top[-1]
        else:
            return 0

    # clear stack
    def clear(self):
        self.top=[]

    # check stack is empty
    def isEmpty(self):
        return len(self.top)==0


n=int(sys.stdin.readline())

par=[0 for i in range(n)]
cur = Stack
cur.__init__(cur)

for i in range(n) :
    par[i] = list(sys.stdin.readline().rstrip())

for i in range(n):
    count = 0
    cur.clear(cur)
    for j in par[i] :
        if j == '(' :
            cur.push(cur,j)
        elif j == ')' :
            if cur.peek(cur) == '(' :
                cur.pop(cur)
            else :
                break
        count+=1
    if count == len(par[i]) and cur.isEmpty(cur) :
        print('YES')
    else :
        print('NO')

