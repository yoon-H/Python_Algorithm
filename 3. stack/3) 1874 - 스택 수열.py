import sys

def push(self, item) :
    self.append(item)

def pop(self) :
    del self[len(self) -1]

def isempty(self) :
    if len(self) == 0 :
        return 1
    else :
        return 0
def peek(self) :
    if isempty(self) :
        return -1
    else :
        return self[len(self) -1]

n= int(sys.stdin.readline())

seq = [0]*n
for i in range(n) :
    seq[i] = int(sys.stdin.readline())

com = list(range(1,n+1))

result =[]
stack = []

for i in seq :
    if peek(stack) > i :
        print('NO')
        break
    else :
        while(1) :
            if peek(stack) == i :          
                pop(stack)
                result.append('-')
                break
            else :
                push(stack, com[0])
                del com[0]
                result.append('+')
        
if len(com) ==0 and len(stack) == 0 :
    for i in result :
        print(i)    