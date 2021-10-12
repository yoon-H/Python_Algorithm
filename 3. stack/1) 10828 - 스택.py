import sys

def push(self, element) :
    self.append(element)

def isempty(self) :
    if len(self) == 0 :
        return 1
    else :
        return 0

def pop(self) :
    if isempty(self) :
        return -1
    else :
        val = self[len(self)-1]
        del self[len(self)-1]
        return val

def size(self) :
    return len(self)

def returntop(self) :
    if isempty(self) :
        return -1
    else :     
        return self[len(self)-1]

n = int(sys.stdin.readline())

stack=[]
command = ['']*n
for i in range(n) :
    command[i] = sys.stdin.readline().rstrip()

for i in command :    
    if 'push' in i :
        push(stack, int(i.split(' ')[1]))
    elif i == 'pop' :
        print(pop(stack))
    elif i == 'size' :
        print(size(stack))
    elif i == 'empty' :
        print(isempty(stack))
    elif i == 'top' :
        print(returntop(stack))

