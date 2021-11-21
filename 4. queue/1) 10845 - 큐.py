import sys

def push(self, item) :
    self.append(item)
    
def pop(self) :
    if len(self) !=0 :
        print(self[0])
        del self[0]
    else:
        print(-1)
    
def size(self) :
    print(len(self))
    
def empty(self) :
    if len(self) ==0 :
        print(1)
    else :
        print(0)
        
def front(self) :
    if len(self) !=0 :
        print(self[0])        
    else:
        print(-1)

def back(self) :
    if len(self) !=0 :
        print(self[-1])
    else:
        print(-1)
        
        
que = []
n= int(sys.stdin.readline())

command = ['']*n

for i in range(n) :
    command[i] = sys.stdin.readline()
     
for i in command :
    if 'push' in i :
        push(que, int(i.split(' ')[1]))
    elif 'pop' in i :
        pop(que)
    elif 'size' in i :
        size(que)
    elif 'empty' in i :
        empty(que)
    elif 'front' in i :
        front(que)
    elif 'back' in i :
        back(que)